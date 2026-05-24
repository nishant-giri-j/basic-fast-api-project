
import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

function handlechange(event){
  console.log("onchange event triggered")
  setPrompt(event.target.value)
}



async function GenerateResponse(){
  const res = await axios.post("http://127.0.0.1:8000/generate", { prompt: prompt })
  setResponse(res.data.response)
}

  return(
    <div className="container">
      <h1>Welcome</h1>

      <textarea onChange={handlechange} placeholder="Enter your prompt here..." rows={10} cols={50} />
      <button onClick={GenerateResponse}>Submit</button>

      <div className="response-box">
        <h2>AI response</h2>
        <p>{response}</p>
        
      </div>
      </div>
  )
}

export default App