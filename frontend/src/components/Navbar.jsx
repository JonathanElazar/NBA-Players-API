import "./css/navbar.css";

function Navbar() {
  return (
    <nav className="nav">
      <a href="/" className="site-title">
        🏀 NBA Players API
      </a>

      <ul>
        <li>
          <a href="/docs">Documentation</a>
        </li>

        <li>
          <a
            href="https://github.com/JonathanElazar/NBA-Players-API"
            target="_blank"
            rel="noopener noreferrer"
          >
            GitHub
          </a>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;