import { useState } from 'react'
import axios, { AxiosError } from 'axios'

export const RegexForm = ({setResponse, setResponseRegex, setErrorMessage}) => {
    const [regex, setRegex] = useState('')

    const sendRegex = async (event) => {
        event.preventDefault()
    
        try {
          const response = await axios.post("http://127.0.0.1:8000/api/dfa", {
            regex: regex
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

    return (
        <>
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
                Käytä sulkeita aina, kun * ja | -operaatioihin liittyvien operandien pituus ylittää yhden merkin.
              </span>
            </span>
          </div>
        </label>
        <div className="button">
          <button type="submit">Luo DFA</button>
        </div>
        </form>
        </>
    )
}