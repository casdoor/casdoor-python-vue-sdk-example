// Copyright 2022 The Casdoor Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import {createRouter, createWebHistory} from "vue-router";
import callbackPage from '../views/callbackPage.vue';
import homePage from '../views/homePage.vue';
import authBox from '../views/authBox.vue';

const routes = [
  {path: '/home', component: homePage,},
  {path: '/callback', component: callbackPage,},
  {path: '/login', component: authBox,}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})
export default router;
