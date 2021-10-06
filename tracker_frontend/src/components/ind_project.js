import React, {useState, useEffect} from "react";
import axios from 'axios';

function ProjectDetail( match ) {
    const [projects, setProject] = useState([]);
    const [project__members, setProjectMembers] = useState([]);

    useEffect(() => {
        fetchProject();
    },[]);

    const fetchProject = async () => {
        axios.get(`http://localhost:8000/tracker_app/project/${match.match.params.project_name}`).then(
            (res) => {
                setProject(res.data)
                setProjectMembers(res.data.members)
            }
        ).catch(err => {
            console.log("Error-cant access")
        })
    };

    return (
        <div>
            {projects.project_name}, project leader: {projects.creator} Project Members : <ul>
            {project__members.map(member => {
                return (
                    <u>
                        <li key="{member}">{member}</li>
                    </u>
                )
            })}
            </ul>
        </div>
    );
}

export default ProjectDetail;

