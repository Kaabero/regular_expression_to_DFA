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

  return (
    <>
      <Notification message={errorMessage} />
      <h2>Säännöllisestä lausekkeesta DFA:ksi</h2>
      <div>
        <RegexForm setResponse={setResponse} setResponseRegex={setResponseRegex} setErrorMessage={setErrorMessage}/>
        {response && (
        <div>
          <DfaChart response={response}/>
          <Dfa responseRegex={responseRegex} response={response} setResponse={setResponse}/>
        </div>
        )}
      </div>
    </>
  )
}

export default App

