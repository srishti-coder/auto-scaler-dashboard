const express = require('express');
const app = express();
const port = 3000;

app.get('/metrics', async (req, res) => {
    try {
        const cpuLoad = 1.89;
        const usedMemory = 4667.77;
        const totalMemory = 7733.50;

        const metrics = 
            `cpuLoad ${cpuLoad}\n` +
            `usedMemoryMB ${usedMemory}\n` +
            `totalMemoryMB ${totalMemory}\n`;

        res.set('Content-Type', 'text/plain');
        res.send(metrics);
    } catch (error) {
        res.status(500).send("Error generating metrics");
    }
});

app.listen(port, () => {
    console.log(`Metrics server running on http://localhost:${port}`);
});
