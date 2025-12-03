import { BaseEdge, BezierEdge, EdgeLabelRenderer } from '@xyflow/react'
 
export const SelfConnectingEdge = (props) => {
  if (props.source !== props.target) {
    return <BezierEdge {...props} />
  }
 
  const { sourceX, sourceY, targetX, targetY, markerEnd, label } = props
  const radiusX = (sourceX - targetX) * 0.6
  const radiusY = 50
  const edgePath = `M ${sourceX - 5} ${sourceY} A ${radiusX} ${radiusY} 0 1 0 ${
    targetX + 2
  } ${targetY}`

  const labelX = sourceX + 5
  const labelY = sourceY - radiusY
 
  return (
    <>
      <BaseEdge path={edgePath} markerEnd={markerEnd}/>
      <EdgeLabelRenderer>
          <div style={{ position: 'absolute', left: `${labelX}px`, top: `${labelY}px`}}>
              <div  className="edge" style={{ padding: '2px 2px', backgroundColor: 'white', fontSize: 10 }}>
                {label}
              </div>
            </div>
      </EdgeLabelRenderer>
    </>
  )
}