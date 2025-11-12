import { useState } from 'react'
import axios, { AxiosError } from 'axios'
import './App.css'

function App() {
  const [regex, setRegex] = useState('')
  const [response, setResponse] = useState(null)
  const [responseRegex, setResponseRegex] = useState('')
  const [errorMessage, setErrorMessage] = useState('')


  const sendRegex = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/dfa", {
        regex: regex,
      })
      setResponse(response.data.result)
      setResponseRegex(response .data.regex)
      setRegex("")
    } catch (error) {
      if (error instanceof AxiosError) {
        setErrorMessage(
          error.response.data.detail || "Virhe palvelimella."
        )
        setResponse('')
        setResponseRegex('')
        setTimeout(() => {
          setErrorMessage('')
        }, 5000)      
        
      } else {
        setErrorMessage("Odottamaton virhe tapahtui.")
        setResponse('')
        setResponseRegex('')
        setTimeout(() => {
          setErrorMessage('')
        }, 5000)
      }
    }
  }

  const Notification = ({message}) => {
    if (message != '') {
      return (
        <div className="notification">
            <p> { message } </p>
        </div>
      )
    }
  }

  return (
    <>
      <Notification message={errorMessage} />
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
                Aakkosto voi sisältää isoja ja pieniä kirjaimia (a-z ja A-Z) sekä numeroita. <br/>
                Lisäksi lauseke voi sisältää tyhjä merkin (€) sekä sulkumerkit. <br/>
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

