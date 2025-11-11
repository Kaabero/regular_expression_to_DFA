import { useState } from 'react'
import './App.css'

function App() {
  const [regex, setRegex] = useState('')
  const [response, setResponse] = useState(null)
  const [responseRegex, setResponseRegex] = useState('')

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
    setResponseRegex(data.regex)
    setRegex("")
  }

  return (
    <>
      <h2>Säännöllisestä lausekkeesta DFA:ksi</h2>
      <div>
        <form className="form-field" onSubmit={sendRegex}>
        <label>
          Syötä säännöllinen lauseke:
          <div className="input">
            <input
              type="text"
              value={regex}
              onChange={(event) => setRegex(event.target.value)}
            />
            <span className="info-icon">
              ?
              <span className="info-text">
                Sallitut operaatiot: <br/>
                - yhdiste | <br/>
                - konkatenaatio (jätetään merkitsemättä) <br/> 
                - tähti * <br/>
                Tyhjä merkki: € <br/>
                Lausekkeen aakkosto ei voi sisältää merkkiä . tai merkkiä #
              </span>
            </span>
          </div>
        </label>
        <div className="button">
          <button type="submit">Luo DFA</button>
        </div>
        </form>

        {response && (
        <div>
          <ul style={{ listStyleType: "none", padding: 0 }}>
            Säännöllisen lausekkeen {responseRegex} syntaksipuu:
            {Object.entries(response).map(([number, node]) => (
              <li key={number}>
              <strong>Node {number}</strong><br />
              Merkki: {node.character}<br />
              Oikea lapsi: {node.right != null ? node.right : 'Ei oikeaa lasta'} <br />
              Vasen lapsi: {node.left != null ? node.left : 'Ei vasenta lasta'} <br />
              Vanhempi: {node.parent != null ? node.parent : 'Ei vanhempaa'} <br />

              </li>
            ))}
          </ul>
        </div>
      )}
      </div>
    </>
  )
}

export default App

