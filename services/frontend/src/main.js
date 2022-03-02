import PrimeVue from 'primevue/config';
import Dropdown from 'primevue/dropdown';
import Tooltip from 'primevue/tooltip';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

const app = createApp(App);
app.use(store);
app.use(router);

app.use(PrimeVue);
app.directive('tooltip', Tooltip);
app.use(Dropdown);

app.mount('#app');
