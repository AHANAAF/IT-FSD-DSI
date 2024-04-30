import { createServer } from 'http';
const hostname = '127.0.0.1';
const port = 3000;

const server = createServer((req, res) => {
    console.log('Received request...', req.url, req.method);

    if (req.url == '/signup') {
        if (req.method == 'POST') {
            let data = '';
            req.on('data', chunk => {
                data += chunk.toString();
            });

            req.on('end', () => {
                const { username, password } = JSON.parse(data);
                console.log('Received signup request for:', username, password);

                res.statusCode = 200;
                res.setHeader('Content-Type', 'application/json');
                res.setHeader('Access-Control-Allow-Origin', '*');
                res.end(JSON.stringify({ message: 'Signup successful' }));
            });
        } else {
            res.statusCode = 405;
            res.end('Method Not Allowed');
        }
    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }
});

server.listen(port, hostname, () => {
    console.log(Server running at http://${hostname}:${port}/);
});