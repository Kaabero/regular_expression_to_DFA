import { useState } from 'react'
import './App.css'

function App() {
  const [regex, setRegex] = useState("")
  const [response, setResponse] = useState("")

  const sendRegex = async (event) => {
    event.preventDefault()
    const res = await fetch("http://127.0.0.1:8000/api/regex", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ regex: regex }),
    })
    const data = await res.json()
    setResponse(data.result)
    setRegex("")
  }

  return (
    <>
      <h2>Säännöllisestä lausekkeesta DFA:ksi</h2>
      <div>
        <form onSubmit={sendRegex}>
          Syötä säännöllinen lauseke:<input type='text' value={regex} onChange={(event) => setRegex(event.target.value)}/>
          <br />
          <button type="submit">Luo DFA</button>
        </form>
      
        {response && (
        <ul style={{listStyleType:'none', padding: 0, margin: 0}}>
          Regexin komponentit:
          {response.map((r, index) => 
            <li key={index}>{r}</li>
          )}
          
        </ul>
        )}
      </div>
    </>
  )
}

export default App

