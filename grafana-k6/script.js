import http from "k6/http";
import { sleep } from "k6";

const url = __ENV.url ? __ENV.url : "http://localhost:3000/member";

export const options = {
  vus: __ENV.vus ? __ENV.vus : 10,
  duration: __ENV.duration ? __ENV.duration : "30s",
};

export default function () {
  http.get(url);
  sleep(1);
}
