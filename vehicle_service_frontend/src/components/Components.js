import React, { useEffect, useState } from 'react';
import { getComponents } from '../api';

const Components = () => {
    const [components, setComponents] = useState([]);

    useEffect(() => {
        getComponents().then(response => setComponents(response.data));
    }, []);

    return (
        <div>
            <h2>Registered Components</h2>
            <ul>
                {components.map((component) => (
                    <li key={component.id}>{component.name} - ${component.price}</li>
                ))}
            </ul>
        </div>
    );
};

export default Components;
