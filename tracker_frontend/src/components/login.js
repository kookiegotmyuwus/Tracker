import React from 'react';

import {Redirect} from 'react-router-dom';
import { Form, Button, Grid, Header, Segment } from "semantic-ui-react";


export default function Login() {


  const oauth = () => {
    window.location.href='https://channeli.in/oauth/authorise/?client_id=JnuJPM5FzaNL9lNfA6rHKUzwiuupkcjhzFDYlB1F&redirect_uri=http://localhost:8000/tracker_app/login1/&state=RANDOM_STATE_STRING'
  }
  return (
    <div>

      <Grid centered>
        <Grid.Column style={{ maxWidth: 550, marginTop: 20 }}>

          <Segment>
            <Form>
              <Button
                onClick={oauth}
                // disabled={registerFormValid || loading}
                fluid
                // loading={loading}
                primary
                type="submit"
              >
                Sign in with Omniport
              </Button>
            </Form>
          </Segment>
        </Grid.Column>
      </Grid>
      
      {/* {http.get("/")} */}
      {/* {console.log(http.get("/"))} */}
    </div>
  );
//   }
}