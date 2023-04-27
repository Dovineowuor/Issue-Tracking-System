import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { Provider } from 'react-redux';
import { configureStore, combineReducers } from '@reduxjs/toolkit';
import App from './App';
import reportWebVitals from './reportWebVitals';

//reducers
import  authReducer from './Controlers/Redux/authSlice'
import  bugReducer from './Controlers/Redux/bugSlice'
import  userReducer from './Controlers/Redux/userSlice'

//configure redux
const reducer=combineReducers({
    auth:authReducer,
    bugs:bugReducer,
    user:userReducer,
})

const store=configureStore({
    reducer
})

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Provider store={store}>
<App />
    </Provider>
    
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
