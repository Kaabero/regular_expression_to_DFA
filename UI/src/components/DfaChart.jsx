import { useState, useCallback, useEffect } from 'react'
import { ReactFlow, applyNodeChanges, applyEdgeChanges, addEdge, Position, MarkerType } from '@xyflow/react'
import '@xyflow/react/dist/style.css'
import { SelfConnectingEdge } from './SelfConnectingEdge'
import { BiDirectionalEdge } from './BiDirectionalEdge'

const edgeTypes = { 
    selfconnecting: SelfConnectingEdge,
    bidirectional: BiDirectionalEdge
}
/*
const initialNodes = [ 
    { id: '1', position: { x: 0, y: 0 }, data: { label: 'Aloitustila 1' }, style: {border: "1px solid black", width: 80}, sourcePosition: Position.Right, targetPosition: Position.Left }, 
    { id: '2', position: { x: 120, y: 80 }, data: { label: '2' }, style: {border: "1px solid black", width: 80 },sourcePosition: Position.Right, targetPosition: Position.Left, }, 
    { id: '3', position: { x: 240, y: 160 }, data: { label: '3' }, style: {border: "1px solid black", width: 80}, sourcePosition: Position.Right, targetPosition: Position.Left, }, 
    { id: '4', position: { x: 360, y: 240 }, data: { label: '4' }, style: {border: "3px solid black", backgroundColor: 'lightgreen', width: 80}, sourcePosition: Position.Right, targetPosition: Position.Left } 
]

const initialEdges = [
    { id: '0', source: '1', target: '2', label: 'a', markerEnd: { type: MarkerType.Arrow }, type: 'default' },
    { id: '1', source: '2', target: '2', label: 'a', markerEnd: { type: MarkerType.Arrow }, type: 'selfconnecting' },
    { id: '2', source: '2', target: '3', label: 'b', markerEnd: { type: MarkerType.Arrow }, type: 'bidirectional'},
    { id: '3', source: '3', target: '2', label: 'a', markerEnd: { type: MarkerType.Arrow }, type: 'bidirectional'},
    { id: '4', source: '3', target: '4', label: 'b', markerEnd: { type: MarkerType.Arrow }, type: 'default' },
    { id: '5', source: '4', target: '2', label: 'a', markerEnd: { type: MarkerType.Arrow }, type: 'default' },
    { id: '6', source: '4', target: '1', label: 'b', markerEnd: { type: MarkerType.Arrow }, type: 'default' },
    { id: '7', source: '1', target: '1', label: 'b', markerEnd: { type: MarkerType.Arrow }, type: 'selfconnecting' },
]

*/
export const DfaChart = ({response}) => {

  

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
                label: transition.character,
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
    )
}
