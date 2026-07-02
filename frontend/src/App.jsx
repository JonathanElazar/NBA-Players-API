import { useState } from 'react'
import './App.css'
import Navbar from './components/navbar'
import terminalGIF from './assets/terminal.gif'

function App() {
  return (
    <div className="App">
      <div>
        <Navbar />
      </div>
      
      <div className="terminalGIF-container">
        <img classname="TerminalGIF" src={terminalGIF} alt="Terminal GIF" className="terminal-gif" />
      </div>

      <div>
        <h3>Welcome to the NBA Players API</h3>
        <p>NBA Players API is a simple REST API for retrieving NBA player statistics. This project is designed to help developers easily integrate player data into their own applications, websites, and projects.</p>
        <p>Feel free to do a simple example request to the API with the following command:</p>

        <div className="terminal">
          <div className="line">$ curl "https://nba-players-api.onrender.com/name/jaylen/brown"</div>
        </div>

        <p>Or you can just go to <a href="https://nba-players-api.onrender.com/name/jaylen/brown" target="_blank" rel="noopener noreferrer">https://nba-players-api.onrender.com/name/jaylen/brown</a> to view the response in your browser.</p>
        <p>If you would like to use this API in your own project, please refer to the documentation or github for more information.</p>
      </div>
    </div>

  )
}

export default App
