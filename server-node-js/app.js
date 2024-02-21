const express = require('express');
const cors = require('cors'); // Importa el módulo cors
const app = express();

// Usa cors middleware
app.use(cors());

// Define tus rutas y lógica de la aplicación
app.get('/check', (req, res) => {
    res.status(200).json({ Estado: 'Check endpoint status: OK!!' });
});

app.get('/', (req, res) => {
    res.json(
        {
            Instancia: 'Instancia #1 - API #1',
            Curso: 'Seminario de Sistemas 1',
            Estudiante: 'Henrry David Bran Velasquez - 201314439'
        });
});

const port = 5000;
app.listen(port, () => {
    console.log(`La aplicación está escuchando en http://localhost:${port}`);
});
