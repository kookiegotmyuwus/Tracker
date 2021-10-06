import React from "react";
import { useLocation } from "react-router";
import { Menu, Image, Button, Icon, Dropdown, Header } from "semantic-ui-react";

const options = [
    {
      key: 'today',
      text: 'today',
      value: 'today',
      content: 'Today',
    },
    {
      key: 'this week',
      text: 'this week',
      value: 'this week',
      content: 'This Week',
    },
    {
      key: 'this month',
      text: 'this month',
      value: 'this month',
      content: 'This Month',
    },
  ]

const Headers = () => {
  const location=useLocation();

  console.log("pathname ",location.pathname)
  return (
    <Menu secondary pointing>
      <Menu.Item style={{ fontSize: 17 }} position="center">
        Tracker
      </Menu.Item>
      {location.pathname !="/" && (<Menu.Item>
        <Header as="h4">
          <Icon name="theme"/>
          <Header.Content >
            <Dropdown
              inline
              header="Adjust time span"
              options={options}
              defaultValue={options[0].value}
            />
          </Header.Content>
        </Header>
      </Menu.Item>)}
    </Menu>
  );
};

export default Headers;
