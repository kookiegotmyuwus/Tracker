import React from 'react';
import { Redirect } from 'react-router-dom';


const Token = (props) => {
    let url_string = window.location.href;
    let url = new URL(url_string);
    let key = url.searchParams.get('token');
    
    let i1=key.indexOf(':');
    let i2=key.indexOf(">");
    let key1=key.slice(i1+2,i2);
    let admin = String(url.searchParams.get('admin'));
    let username = String(url.searchParams.get('username'));
    let auth = 'Token '.concat(String(key1));

    props.settoken(auth);
    admin = (admin === "True" ? true : false);
    sessionStorage.setItem('token', auth);
    sessionStorage.setItem('admin', admin);
    sessionStorage.setItem('username', username);
    props.setlogin(true);
    props.setadmin(admin);
    props.setuser(username);

    return (
        <h1>hello</h1>
        // <Redirect to="/" />
    );
}

export default Token;