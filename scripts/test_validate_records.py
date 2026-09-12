import tempfile
import unittest
from pathlib import Path
from validate_records import validate, incomplete

class ValidationTests(unittest.TestCase):
    def test_evidence_cases(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'clientes').mkdir()
            (root / 'evidencias').mkdir()
            (root / 'evidencias/real.md').write_text('Resultado verificado')
            (root / 'evidencias/empty.md').touch()
            for evidence, expected in [('', True), ('`evidencias/<slug>/prueba.md`', True),
                ('`evidencias/missing.md`', True), ('`evidencias/empty.md`', True),
                ('`../outside.md`', True), ('`TASKS.md`', True),
                ('`evidencias/real.md`', False)]:
                with self.subTest(evidence=evidence):
                    (root / 'TASKS.md').write_text('| ID | Estado | Criterio | Evidencia |\n'
                        f'| P-001 | completa | Ver `informe.md` | {evidence} |\n')
                    self.assertEqual(bool(validate(root)[0]), expected)
            (root / 'TASKS.md').write_text('| ID | Estado | Criterio |\n| P-001 | completa | `informe.md` |')
            self.assertTrue(validate(root)[0])
            (root / 'TASKS.md').write_text('| ID | Estado | Resultado |\n| P-001 | pendiente | Caracterización completa |')
            self.assertFalse(validate(root)[0])

    def test_placeholders(self):
        for value in ['', '—', '_pendiente_', 'nombre, cargo, teléfono, email.', '<contacto>', 'por confirmar']:
            self.assertTrue(incomplete(value), value)
        self.assertFalse(incomplete('Contacto de prueba confirmado'))

if __name__ == '__main__':
    unittest.main()
