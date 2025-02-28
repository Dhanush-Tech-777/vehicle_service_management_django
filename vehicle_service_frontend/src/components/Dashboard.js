import React, { useEffect, useState } from 'react';
import { getRepairs } from '../api';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const Dashboard = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        getRepairs().then(response => {
            const transformedData = response.data.map((repair, index) => ({
                name: `Repair ${index + 1}`,
                cost: repair.total_cost
            }));
            setData(transformedData);
        });
    }, []);

    return (
        <div>
            <h2>Revenue Overview</h2>
            <ResponsiveContainer width="100%" height={300}>
                <BarChart data={data}>
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="cost" fill="#8884d8" />
                </BarChart>
            </ResponsiveContainer>
        </div>
    );
};

export default Dashboard;
