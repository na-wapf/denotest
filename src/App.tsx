import {  useState } from "react"
import { FullFeaturedCrudGrid } from "./EditableGrid"


function App() {
    const [count, setCount] = useState(0)


    return (
        <>

            <SpecialButton
                count={count}
                onClick={() => setCount(v => v + 1)}
            ></SpecialButton>
            <hr/>
            <FullFeaturedCrudGrid/>
        </>
    )
}

export default App


function SpecialButton(props: { count: number, onClick: () => void }) {
    return <button onClick={() => props.onClick()}>
        count is {props.count}
    </button>
}