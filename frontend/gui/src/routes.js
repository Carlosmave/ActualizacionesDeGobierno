import React from 'react';
import { Route } from 'react-router-dom';

import RegionList from './containers/RegionListView';
import RegionDetail from './containers/RegionDetailView';
import ProvinceDetail from './containers/ProvinceDetailView';
import PoliticianDetail from './containers/PoliticianDetailView';



const BaseRouter = () => (
    <div>
        <Route exact path='/' component={RegionList} />
        <Route exact path='/regions/:regionID' component={RegionDetail} />
        <Route exact path='/provinces/:provinceID' component={ProvinceDetail} />
        <Route exact path='/politicians/:politicianID' component={PoliticianDetail} />
    </div>

);

export default BaseRouter;
