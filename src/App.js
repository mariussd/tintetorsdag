import React from "react";
import logo from "./images/logo.png";
import "./App.scss";

const App = () => {
  return (
    <div>
      <div class="flexbox">
        <a
          href="https://www.facebook.com/groups/320621909163662"
          target="_blank"
          rel="noopener noreferrer"
          alt="logo"
        >
          <div class="flexbox">
            <img
              src={logo}
              alt="Logoen til Tintetorsdag"
              width="25%"
              height="25%"
            />
          </div>
        </a>
        <h1 id="main-heading">Aldri sint med en tint!</h1>
        <br />
        <p>
          Stiftet av Magnus Rand og Marius Sørensen Dreyer i det Herrens år
          2020.
        </p>
      </div>
    </div>
  );
};

export default App;
