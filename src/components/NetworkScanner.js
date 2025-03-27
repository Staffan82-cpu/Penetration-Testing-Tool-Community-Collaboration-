import React, { useState } from "react";
import axios from "axios";
import { Button, TextField, Typography, Container } from "@mui/material";

function NetworkScanner() {
  const [ipRange, setIpRange] = useState("192.168.1.1/24");
  const [results, setResults] = useState([]);

  const handleScan = async () => {
    const res = await axios.post("http://localhost:5000/scan", { ip_range: ipRange });
    setResults(res.data);
  };

  return (
    <Container>
      <Typography variant="h4">🛡️ Network Scanner</Typography>
      <TextField label="IP Range" value={ipRange} onChange={(e) => setIpRange(e.target.value)} />
      <Button variant="contained" color="primary" onClick={handleScan}>Scan</Button>
      <ul>
        {results.map((device, index) => (
          <li key={index}>{device.IP} - {device.MAC}</li>
        ))}
      </ul>
    </Container>
  );
}

export default NetworkScanner;
