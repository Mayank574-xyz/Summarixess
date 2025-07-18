const root = document.getElementById("root");

root.innerHTML = `
  <div style="max-width:700px;margin:2rem auto;padding:1rem;font-family:sans-serif;text-align:center;">
    <h1>🧠 AI Text Summarizer</h1>
    <textarea id="input" placeholder="Paste your text here..." style="width:100%;height:150px;padding:10px;margin-top:10px;resize:none;"></textarea>
    <br/>
    <button id="btn" style="margin-top:15px;padding:10px 20px;background:#007bff;color:white;border:none;cursor:pointer;">Summarize</button>
    <div id="output" style="margin-top:20px;background:#f3f3f3;padding:1rem;text-align:left;white-space:pre-wrap;"></div>
    <p style="margin-top:30px;font-size:0.85rem;color:gray;">⚠️ Review AI summaries before using them.</p>
  </div>
`;

document.getElementById("btn").addEventListener("click", async () => {
  const text = document.getElementById("input").value.trim();
  const output = document.getElementById("output");

  if (!text) {
    output.innerText = "Please enter some text.";
    return;
  }

  output.innerText = "Summarizing...";

  try {
    const res = await fetch("/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await res.json();
    output.innerText = data.summary || "No summary received.";
  } catch (err) {
    output.innerText = "❌ Error contacting server.";
  }
});
