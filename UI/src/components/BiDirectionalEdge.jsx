import { getBezierPath, useStore, BaseEdge, EdgeLabelRenderer } from '@xyflow/react'


export const BiDirectionalEdge = (props) => {
  const { id, source, target, sourceX, sourceY, targetX, targetY, label, markerEnd } = props

  const getSpecialPath = ({ sourceX, sourceY, targetX, targetY }, offset ) => {
    const centerX = (sourceX + targetX) / 2
    const centerY = (sourceY + targetY) / 2
    return `M ${sourceX} ${sourceY} Q ${centerX} ${centerY + offset} ${targetX} ${targetY}`
  }


  const isBiDirectionEdge = useStore((s) => {
    const edgeExists = s.edges.some(
      (e) =>
        ((e.source === target && e.target === source) ||
        (e.target === source && e.source === target)) &&
        e.id !== id
    )
    return edgeExists
  })

  const edgePathParams = { sourceX, sourceY, targetX, targetY }

  let path = ''
  let labelX = (sourceX + targetX) / 2
  let labelY = (sourceY + targetY) / 2


  if (isBiDirectionEdge) {
    const offset = sourceX < targetX ? 25 : -25
    path = getSpecialPath(edgePathParams, offset)
    labelY = labelY + offset / 2
  } else {
    const [bezPath, lx, ly] = getBezierPath(edgePathParams)
    path = bezPath
    labelX = lx
    labelY = ly
  }


  return (
    <>
      <BaseEdge path={path} markerEnd={markerEnd} />
        <EdgeLabelRenderer>
          <div style={{ position: 'absolute', left: `${labelX}px`, top: `${labelY}px`, transform: `translate(-50%, -50%)`, whiteSpace: 'nowrap'}}>
            <div style={{ padding: '2px 2px', backgroundColor: 'white', fontSize: 10 }}>
              {label}
            </div>
          </div>
        </EdgeLabelRenderer>
    </>
  )
}