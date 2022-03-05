import 'primeicons/primeicons.css';
import Button from 'primevue/button';
import Card from 'primevue/card';
import PrimeVue from 'primevue/config';
import Dropdown from 'primevue/dropdown';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/lara-light-blue/theme.css';
import Tooltip from 'primevue/tooltip';
import { createApp } from 'vue';
import App from './App.vue';
import AlertBox from './components/error/AlertBox.vue';
import './index.css';
import router from './router';
import store from './store';



const app = createApp(App);
app.use(store);
app.use(router);
app.use(PrimeVue);

app.component('Button', Button);
app.component('Card', Card);
app.component('Dropdown', Dropdown);
app.component('InputText', InputText);
app.component('Password', Password);
app.component('AlertBox', AlertBox);
app.directive('tooltip', Tooltip);

app.mount('#app');
