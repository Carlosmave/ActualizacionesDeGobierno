import React from 'react';
import axios from 'axios';
import { PageHeader } from 'antd';

import Comments from '../components/Comments';
import CustomForm from '../components/Form';


class PoliticianDetail extends React.Component {

  state = {
      comments: [],
      politician: {}
    }

  componentDidMount() {
    const politicianID = this.props.match.params.politicianID;
    axios.get(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`)
        .then(res => {
            this.setState({
              comments: res.data
            });
            console.log(res.data);
        })
    axios.get(`http://127.0.0.1:8000/politicians/${politicianID}/`)
        .then(res => {
            this.setState({
              politician: res.data
            });
            console.log(res.data);
        })
  }


  render() {
    return(
      <div>
        <CustomForm
          politicianID={this.props.match.params.politicianID} />
        <br />
        <PageHeader
          style={{
            border: '1px solid rgb(235, 237, 240)',
          }}
          title={"Comentarios de " + this.state.politician.poli_name}
        />
        <Comments data={this.state.comments} />
      </div>
    )
  }
}

export default PoliticianDetail
