import { useState } from 'react'
import './App.css'
import { Notification } from './components/Notification'
import { RegexForm } from './components/RegexForm'
import { Dfa } from './components/Dfa'
import { DfaChart } from './components/DfaChart'


function App() {

  const [response, setResponse] = useState(null)
  const [responseRegex, setResponseRegex] = useState('')
  const [errorMessage, setErrorMessage] = useState('')
  const [showChart, setShowChart] = useState(false)

  return (
    <>
      <Notification message={errorMessage} />
      <h2>Säännöllisestä lausekkeesta DFA:ksi</h2>
      <div>
        {!response ? (
            <RegexForm setResponse={setResponse} setResponseRegex={setResponseRegex} setErrorMessage={setErrorMessage}/>
        ) : (
          <div>
            {showChart ? (
              <>
              <button onClick={() => setShowChart(false)}>Näytä tiedot</button>
              <button onClick={() => setResponse(null)}>Aloita alusta</button>
              <DfaChart responseRegex={responseRegex} response={response}/>
              </>
            ) :
            <>
            <button onClick={() => setShowChart(true)}>Näytä kuva</button>
            <button onClick={() => setResponse(null)}>Aloita alusta</button>
            <Dfa responseRegex={responseRegex} response={response}/>
          
            </>
            }
          </div>
        )}
      </div>
    </>
  )
}

export default App

