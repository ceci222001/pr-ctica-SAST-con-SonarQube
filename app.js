const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Pipeline CI/CD funcionando correctamente");
});

app.listen(3000, () => {
  console.log("Servidor ejecutándose en puerto 3000");
});
