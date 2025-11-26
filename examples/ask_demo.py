"""Demo RAG sencillo en memoria.

Ejecuta:
  py .\examples\ask_demo.py

El script indexa dos documentos y responde preguntas buscando la frase más similar.
"""
import difflib


DOCS = [
    {
        'id': 'doc1',
        'text': 'La política de privacidad establece que los datos personales se conservarán por un periodo de cinco años. ' 
                'Los usuarios pueden solicitar la eliminación de datos mediante el formulario de contacto.'
    },
    {
        'id': 'doc2',
        'text': 'La garantía cubre defectos de fabricación por un periodo de 24 meses desde la compra. ' 
                'No cubre daños por mal uso o modificación del producto.'
    }
]


def retrieve(query):
    # similitud simple por ratio de SequenceMatcher
    best = None
    best_score = 0.0
    for d in DOCS:
        score = difflib.SequenceMatcher(a=query.lower(), b=d['text'].lower()).ratio()
        if score > best_score:
            best_score = score
            best = d
    return best, best_score


def generate_answer(query, doc):
    return f"Basado en {doc['id']}: {doc['text'][:200]}...\nRespuesta: Según el documento, {doc['text'].split('.')[0]}."


def main():
    print('Demo Ask (RAG) - indexando documentos...')
    print('Documentos cargados:', [d['id'] for d in DOCS])

    queries = [
        '¿Cuánto tiempo se conservan los datos personales?',
        '¿La garantía cubre daños por mal uso?'
    ]
    for q in queries:
        print('\nPregunta:', q)
        doc, score = retrieve(q)
        print(f'Recuperado: {doc["id"]} (score={score:.2f})')
        ans = generate_answer(q, doc)
        print('Respuesta generada:\n', ans)


if __name__ == '__main__':
    main()
