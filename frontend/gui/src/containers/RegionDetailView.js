import React from 'react';
import axios from 'axios';
import { PageHeader } from 'antd';

import Politicians from '../components/Politicians';

class RegionDetail extends React.Component {

  state = {
      politicians: [],
      region: {}
    }

  componentDidMount() {
    const regionID = this.props.match.params.regionID;
    axios.get(`http://127.0.0.1:8000/regionsdetails/${regionID}`)
        .then(res => {
            this.setState({
              politicians: res.data
            });
            console.log(res.data);
        })
    axios.get(`http://127.0.0.1:8000/regions/${regionID}`)
        .then(res => {
            this.setState({
              region: res.data
            });
            console.log(res.data);
        })
  }

  render() {
    return(
      <div>
      <PageHeader
        style={{
          border: '1px solid rgb(235, 237, 240)',
        }}
        title= {"Actuales Autoridades Regionales de " + this.state.region.reg_name}
      />
      <br />
      <Politicians data={this.state.politicians} />
      </div>
    )
  }
}

export default RegionDetail
