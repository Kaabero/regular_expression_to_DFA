export const Dfa = ({responseRegex, response, setResponse}) => {

    const states = response ? response.states.join(', ') : ''
    const alphabet = response ? response.alphabet.join(', ') : ''
    const accepting_states = response ? response.accepting_states.join(', ') : ''

    return (
        <div>
            <h3>Säännöllisen lausekkeen DFA:</h3>
            <strong>Lauseke: </strong>{responseRegex} <br/>
            <strong>Tilat: </strong>{'{'}{states}{'}'}
            <br/>
            <strong>Aakkosto: </strong>{alphabet.length > 0 ? <>{'{'}{alphabet}{'}'}</> : <>Tyhjä aakkosto</>}
            <br />
            <strong>Siirtymät: </strong>           
            {Object.entries(response.transitions).length > 0 ? (
              Object.entries(response.transitions).map(([number, transition]) => (
                <li style={{listStyleType: "none"}} key={number}>
                  δ({transition.from}, {transition.character})={transition.to}
                </li>
              ))
            ) : (
            <>Ei siirtymiä. <br/></> 
            )}
            
            <strong>Alkutila: </strong>{response.q_0} <br/>
            <strong>Hyväksyvät tilat: </strong>{'{'}{accepting_states}{'}'}
            <div className="button">
                <button onClick={() => setResponse(null)}>Tyhjennä</button>
            </div>
        </div>
    )
}