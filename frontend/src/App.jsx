import { useState, useEffect } from 'react'
import '../style.css'

function App() {
  const [count, setCount] = useState(0);
  const [texts, setTexts] = useState([]);
  const [selectedTextID, setSelectedTextID] = useState("");
  const [text, setText] = useState("");

  useEffect(()=> {
    // update selection list on render
    //console.log(text)
    loadSelectedList();

  }, []);

  async function loadSelectedList() {
    try {
      // await response from the backend
      const response = await fetch("/api/text/list");
      //await for response and save the data
      const data = await response.json();

      if (data.ok) {
        setTexts(data.texts);
      }
    } catch (error) {
      console.error("Failed to load text list:",error);
    }
  }

  async function loadText() {
    if (!selectedTextID) return;

    const response = await fetch(`/api/text/${selectedTextID}/load`, {
      method: "GET",
    });

    const data = await response.json();
    if (data.ok) {
      setText(data.content)
    } else {
      alert("Load failed.");
      return;
    }
  }

  async function saveText() {
    const name = window.prompt("Canvas name:");
    if (!name) return;

    const response = await fetch("/api/text/save", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({name,content: text})
    });
    
    const data = await response.json();

    if (!data.ok) {
      alert("Save failed.");
      return;
    }

    alert("Text saved.");
    await loadSelectedList();

  }

  return (
    <main>
      <div id="custom">
        <div style={{backgroundColor: "coral"}}>A</div>
        <div style={{backgroundColor: "aquamarine"}}>B</div>
        <div style={{backgroundColor: "khaki"}}>C</div>
        <div style={{backgroundColor: "pink"}}>D</div>
        <div style={{backgroundColor: "lightgrey"}}>E</div>
        <div style={{backgroundColor: "lightgreen"}}>F</div>
      </div>
      <form>
        <label style={{color: "white"}} htmlFor="words">Say something</label><br />
        <input type="text" id="words" name="words" value={text} onChange={(event) => setText(event.target.value)}></input>
      </form>
      <button onClick={saveText}>Save Text</button>
    
      <select
        value={selectedTextID}
        onChange={(event) => setSelectedTextID(event.target.value)}
      >
        <option value = "">Select saved text</option>
        {texts.map((text) => (
          <option key = {text.id} value = {text.id}>
            {text.name}
          </option>
        ))}
      </select>
      <button onClick={loadText}>Load Text</button>
    </main>
  )
}

export default App
