import React, { useState } from "react";
import "simplebar"; // or "import SimpleBar from 'simplebar';" if you want to use it manually.
import "simplebar/dist/simplebar.css";
// import ReactDOM from "react-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import Content from "./Content";
import MessageExampleAttached from "./example";
import "semantic-ui-css/semantic.min.css";
import "./styles.css";

function Dashboard() {
  const [toggleBtn, setToggleBtn] = useState(true);
  const toggle = () => setToggleBtn(val => !val);
  return (
    <div className="top-wrapper">
      <Navbar setToggle={toggle} />
      <Sidebar toggleBtn={toggleBtn} />
      <Content>
        <MessageExampleAttached />
      </Content>
    </div>
  );
}

export default Dashboard;
