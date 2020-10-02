import React from "react";
import logo from "./images/logo.png";
import "./App.scss";

const App = () => {
  return (
    <>
      <header className="header">
        <div className="header-image-container">
          <img src={logo} alt="Logoen til Tintetorsdag" />
        </div>
        <div className="header-title">Tintetorsdag</div>
        <div className="header-login">Logg inn</div>
      </header>
      <div>
        <div className="flexbox">
          <h1 id="main-heading">Aldri sint med en tint!</h1>
          <br />
          <p>
            Stiftet av Magnus Rand og Marius Sørensen Dreyer i det Herrens år
            2020.
          </p>
        </div>
      </div>
    </>
  );
};

export default App;
