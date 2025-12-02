import { useState, useCallback, useEffect } from 'react'
import { ReactFlow, applyNodeChanges, applyEdgeChanges, addEdge, Position, MarkerType } from '@xyflow/react'
import '@xyflow/react/dist/style.css'
import { SelfConnectingEdge } from './SelfConnectingEdge'
import { BiDirectionalEdge } from './BiDirectionalEdge'

const edgeTypes = { 
    selfconnecting: SelfConnectingEdge,
    bidirectional: BiDirectionalEdge
}

export const DfaChart = ({responseRegex, response}) => {
  

    const [nodes, setNodes] = useState([])
    const [edges, setEdges] = useState([])
   

    
    useEffect(() => {
        setNodes(response.states.map((state, index) => ({

                id: state.toString(),
                position: { x: index*120, y: index*80 },
                data: state == response.q_0 ? { label: `Aloitustila ${state.toString()}`} : { label: state.toString() },
                style: response.accepting_states.includes(state) ? {border: "3px solid black", backgroundColor: 'lightgreen', width: 80} : {border: "1px solid black", width: 80 },
                sourcePosition: Position.Right,
                targetPosition: Position.Left
            })
        ))
    }, [response])

    useEffect(() => {
        setEdges(response.transitions.map((transition, index) => ({

                id: index.toString(),
                source: transition.from.toString(),
                target: transition.to.toString(),
                label: transition.labels ? transition.labels.join(', ') : transition.character,
                markerEnd: { type: MarkerType.Arrow },
                type: transition.type
              
            })
        ))
    }, [response])

    
    const onNodesChange = useCallback(
        (changes) => setNodes((nodesSnapshot) => applyNodeChanges(changes, nodesSnapshot)),
        [],
    )
    const onEdgesChange = useCallback(
        (changes) => setEdges((edgesSnapshot) => applyEdgeChanges(changes, edgesSnapshot)),
        [],
    )
    const onConnect = useCallback(
        (params) => setEdges((edgesSnapshot) => addEdge(params, edgesSnapshot)),
        [],
    )
    
    return (
        <>
            <h4>Säännöllisen lausekkeen "{responseRegex}" DFA:</h4>
            <div style={{ width: '100vw', height: '100vh' }}>
            <ReactFlow
                nodes={nodes}
                edges={edges}
                edgeTypes={edgeTypes}
                onNodesChange={onNodesChange}
                onEdgesChange={onEdgesChange}
                onConnect={onConnect}
                fitView
            />
            </div>
        </>
    )
}
