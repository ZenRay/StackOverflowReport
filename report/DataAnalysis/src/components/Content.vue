<template>
  <div class="col-md-9 col-sm-8" id="main-content">
    <section v-for="(val, key) in contentlist" :key="key.id" v-bind="{ id: key}">
      <div class="section-intro _background-light">
        <div class="color-bar">
          <span class="_color-bar-orange"></span>
          <span class="_color-bar-amber"></span>
          <span class="_color-bar-yellow"></span>
        </div>
        <div class="section-intro-content">
          <div class="section-intro-icon">
            <svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 182.61892 95.30279">
              <title>{{key}}</title>
              <path d="M172.37049,14.66836a5.775,5.775,0,0,0-.851.06973,10.69887,10.69887,0,0,0-21.34985.02165,5.75783,5.75783,0,1,0-.99311,11.429c.14046,0,.2781-.01114.416-.021a4.00548,4.00548,0,0,0,.41121.021h21.72967c.1051,0,.20827-.00943.312-.0164.10822.00607.21532.0164.32508.0164a5.76017,5.76017,0,1,0,0-11.52033Z" style="fill:none;stroke:#aee0ff;stroke-miterlimit:10;stroke-width:0.75px"></path>
              <path d="M34.391,71.61866a4.24134,4.24134,0,0,0-.62512.05123,7.8588,7.8588,0,0,0-15.68242.0159,4.22938,4.22938,0,1,0-.72949,8.39508c.10318,0,.20428-.00819.3056-.01544a2.94091,2.94091,0,0,0,.302.01544H33.92306c.0772,0,.153-.00694.22919-.01205.07948.00446.15816.01205.23878.01205a4.23111,4.23111,0,0,0,0-8.46221Z" style="fill:none;stroke:#aee0ff;stroke-miterlimit:10;stroke-width:0.75px"></path>
              <path d="M31.671,15.07268a2.88748,2.88748,0,0,0-.42551.03487,5.34944,5.34944,0,0,0-10.67493.01082,2.87892,2.87892,0,1,0-.49655,5.71448c.07023,0,.139-.00558.208-.01051a2.00283,2.00283,0,0,0,.20561.01051H31.35247c.05255,0,.10414-.00472.156-.0082.0541.003.10766.0082.16253.0082a2.88009,2.88009,0,1,0,0-5.76017Z" style="fill:none;stroke:#aee0ff;stroke-miterlimit:10;stroke-width:0.75px"></path>
              <path d="M139.38716,71.93106a1.40651,1.40651,0,0,0-.24718.02428,3.12079,3.12079,0,1,0-6.2009.00754,1.40762,1.40762,0,0,0-.28844-.03182,2.03893,2.03893,0,0,0,0,4.01165c.04079,0,.08077-.00388.12083-.00731a.97292.97292,0,0,0,.11943.00731h6.31122c.03053,0,.06049-.00328.09062-.00571.03143.00211.06254.00571.09442.00571a2.03893,2.03893,0,0,0,0-4.01165Z" style="fill:none;stroke:#aee0ff;stroke-miterlimit:10;stroke-width:0.75px"></path>
              <g id="_Group_" data-name="<Group>">
                <polygon id="_Path_" data-name="<Path>" points="113.686 32.989 126.359 28.144 114.542 22.235 113.686 32.989" style="fill:#ffb935"></polygon>
                <polygon id="_Path_2" data-name="<Path>" points="64.013 21.063 111.281 44.697 74.845 41.743 64.013 21.063" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></polygon>
                <line id="_Path_3" data-name="<Path>" x1="113.25022" y1="20.07851" x2="91.89108" y2="34.99741" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></line>
                <line id="_Path_4" data-name="<Path>" x1="113.25022" y1="20.07851" x2="111.28072" y2="44.69716" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></line>
                <polyline id="_Path_5" data-name="<Path>" points="113.25 20.079 125.067 25.987 112.393 30.832" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></polyline>
                <line id="_Path_6" data-name="<Path>" x1="74.84512" y1="41.74292" x2="64.01292" y2="78.17852" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></line>
                <line id="_Path_7" data-name="<Path>" x1="111.28072" y1="44.69716" x2="64.01292" y2="78.17852" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></line>
                <line id="_Path_8" data-name="<Path>" x1="86.27802" y1="32.19088" x2="77.79936" y2="17.12427" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></line>
                <line id="_Path_9" data-name="<Path>" x1="77.79936" y1="17.12427" x2="77.71073" y2="27.34593" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></line>
                <line id="_Path_10" data-name="<Path>" x1="83.9366" y1="64.06591" x2="74.84512" y2="41.74292" style="fill:none;stroke:#f48024;stroke-linecap:round;stroke-linejoin:round"></line>
                </g>
            </svg>
          </div>

          <div class="setion-intro-body">
            <a v-bind="{href: '#'+key}">
              <h2 class="_orange">{{key}}</h2>
            </a>
            <p class="_lead">{{val}}</p>
          </div>
        </div>
      </div>
      <div class="section-content">
        <p v-bind="{id:key+'context'}">{{testmsg}}</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Content',
  data () {
    return {
      contentlist: {
        Overview: 'Overview context test',
        DeveloperProfile: 'Developer Profile context test'
      },
      testmsg: 'This is test message!'
    }
  }
}
</script>

<style>

</style>
