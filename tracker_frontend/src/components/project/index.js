import React, { useEffect, useState } from 'react'
import axios from 'axios'
// import Loader from 'react-loader-spinner'


const Projects = ({ id, token, users }) => {
    const apiUrl = 'http://127.0.0.1:8000/tracker_app/project/';
    const [projects, setprojects] = useState([])
    // const [loading, setloading] = useState(true)
    const projectList = []
    let myid = parseInt(id)
    useEffect(() => {
        axios.get(apiUrl, {
            headers: {
                'Authorization': token,
            }
        })
            .then(res => {
                // setloading(false)
                console.log(id)
                setprojects(res.data)
            })
            .catch(error => {
                if (error.response) {
                    // setloading(false)
                    // seterror([{ 'details': error.response.data, 'status': error.response.status }])
                }
            })
    }, [apiUrl])
    
    // projects.map(element => {
    //     if (element.team_members.includes(myid) || element.creator.includes(myid)) {
    //         projectList.push(element)
    //     }

    //     return null
    // })
    return (
        <>
        <h1>{id}</h1>
        
            {/* {loading ? <Loader type="ThreeDots" color="black" height={80} width={80} /> :
                <>
                       { projectList.map(element => (
                            <div key={element.id} className="project">
                                <h2 className="heading"> {element.name}</h2>
                                <p className="wiki">{element.wiki.replaceAll('<p>', '').replaceAll('</p>', '\n')}</p>
                                <p><span className="desc">Date Created: </span><span className="details">{element.date_started}</span></p>
                                <div><span className="desc">Team Members: </span>{element.team_members.map(member => (
                                    <p className="details" key={member}>{users.find(o => o.id === member).name}</p>
                                ))}</div>
                                <div><span className="desc">Creator: </span>{element.creator.map(member => (
                                    <p className="details" key={member}>{users.find(o => o.id === member).name}</p>
                                ))}</div>
                            </div>
                        ))
                    }
                </>
            } */}
        </>
    );
};

export default Projects;