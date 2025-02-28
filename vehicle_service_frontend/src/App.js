import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Components from './components/Components';
import Dashboard from './components/Dashboard';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/components" element={<Components />} />
                <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
        </Router>
    );
}

export default App;
