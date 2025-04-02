import React, { useState } from "react";
import axios from "axios";

const App: React.FC = () => {
  const [cryptoPrice, setCryptoPrice] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);

  const fetchCryptoPrice = async () => {
    setLoading(true);
    try {
      const response = await axios.get("http://127.0.0.1:8000/predict"); // Adjust API URL
      setCryptoPrice(response.data.predicted_price);
    } catch (error) {
      console.error("Error fetching crypto price:", error);
    }
    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Crypto Price Prediction</h1>
      <button onClick={fetchCryptoPrice} disabled={loading}>
        {loading ? "Loading..." : "Get Predicted Price"}
      </button>
      {cryptoPrice !== null && (
        <h2>Predicted Price: ${cryptoPrice.toFixed(2)}</h2>
      )}
    </div>
  );
};

export default ATpp;