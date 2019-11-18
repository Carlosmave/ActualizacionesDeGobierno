import React from 'react';
import axios from 'axios';
import { Input, PageHeader } from 'antd';

import Regions from '../components/Regions';


class RegionList extends React.Component {

    state = {
      search: "",
      regions:[]
    }

    componentDidMount() {
      axios.get('http://127.0.0.1:8000/regions/')
          .then(res => {
              this.setState({
                regions: res.data
              });
              console.log(res.data);
          })
    }


    onChange = e => {
      this.setState({ search: e.target.value });
    };

  render() {
    const search = this.state.search;
    const filteredRegions = this.state.regions.filter(region => {
      return region.reg_name.toLowerCase().indexOf(search.toLowerCase()) !== -1;
    });
    const { Search } = Input;
    return(
      <div>
      <PageHeader
        style={{
          border: '1px solid rgb(235, 237, 240)',
        }}
        title="Regiones"
      />
      <br />
      <Search
        placeholder="Buscar región"
        onChange={this.onChange}
      />
      <br />
      <br />
      <Regions data={filteredRegions} />
      </div>
    )
  }
}

export default RegionList
