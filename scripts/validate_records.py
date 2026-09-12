#!/usr/bin/env python3
"""Validate task evidence without displaying client data. Paths use repository root."""
import re
import sys
from pathlib import Path


def table_rows(text):
    header = None
    for line in text.splitlines():
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if cells[0] == 'ID':
            header = cells
        elif header and re.fullmatch(r'[CP]-\d+', cells[0]):
            yield dict(zip(header, cells))


def incomplete(value):
    value = value.strip().strip('_').strip().lower().rstrip('.')
    return (value in ('', '—', '-', 'pendiente', 'por confirmar', 'nombre, cargo, teléfono, email')
            or 'pendiente' in value or '<' in value or 'por confirmar' in value)


def validate(root):
    errors = []
    warnings = []
    for ficha in sorted((root / 'clientes').glob('*/CLIENTE.md')):
        if ficha.parent.name == '_template':
            continue
        text = ficha.read_text()
        for field in ('NIT', 'Contacto principal', 'Ciudad / dirección'):
            match = re.search(r'^- \*\*' + re.escape(field) + r'\*\*:[ \t]*([^\n]*)$', text, re.M)
            if not match or incomplete(match[1]):
                warnings.append(f'{ficha.parent.name}: {field} incompleto')
    tasks = [root / 'TASKS.md', *sorted((root / 'clientes').glob('*/TASKS.md'))]
    for task in tasks:
        if task.parent.name == '_template' or not task.is_file():
            continue
        for row in table_rows(task.read_text()):
            if row.get('Estado') != 'completa':
                continue
            label = f'{task.relative_to(root)}: {row["ID"]}'
            evidence = row.get('Evidencia', '')
            paths = re.findall(r'`([^`]+)`', evidence)
            if not paths:
                errors.append(f'{label}: falta evidencia concreta en columna Evidencia')
                continue
            for value in paths:
                path = (root / value).resolve()
                if (Path(value).is_absolute() or not path.is_relative_to(root.resolve())
                        or not value.startswith(('evidencias/', 'entregables/'))
                        or '<' in value or '>' in value
                        or not path.is_file() or path.stat().st_size == 0):
                    errors.append(f'{label}: evidencia inválida, inexistente o vacía')
                    break
    return errors, warnings


if __name__ == '__main__':
    errors, warnings = validate(Path(sys.argv[1]).resolve())
    for message in warnings:
        print('  warn: ' + message)
    for message in errors:
        print('  ERROR: ' + message)
    print(f'Registros: {len(errors)} errores, {len(warnings)} advertencias')
    sys.exit(bool(errors))
