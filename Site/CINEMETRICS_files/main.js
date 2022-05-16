!function(e){function t(t){for(var o,s,a=t[0],l=t[1],c=t[2],u=0,m=[];u<a.length;u++)s=a[u],Object.prototype.hasOwnProperty.call(i,s)&&i[s]&&m.push(i[s][0]),i[s]=0;for(o in l)Object.prototype.hasOwnProperty.call(l,o)&&(e[o]=l[o]);for(d&&d(t);m.length;)m.shift()();return r.push.apply(r,c||[]),n()}function n(){for(var e,t=0;t<r.length;t++){for(var n=r[t],o=!0,a=1;a<n.length;a++){var l=n[a];0!==i[l]&&(o=!1)}o&&(r.splice(t--,1),e=s(s.s=n[0]))}return e}var o={},i={0:0},r=[];function s(t){if(o[t])return o[t].exports;var n=o[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=e,s.c=o,s.d=function(e,t,n){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},s.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)s.d(n,o,function(t){return e[t]}.bind(null,o));return n},s.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/";var a=window.webpackJsonp=window.webpackJsonp||[],l=a.push.bind(a);a.push=t,a=a.slice();for(var c=0;c<a.length;c++)t(a[c]);var d=l;r.push([70,1]),n()}({1:function(e,t,n){"use strict";n.d(t,"d",(function(){return r})),n.d(t,"e",(function(){return s})),n.d(t,"f",(function(){return a})),n.d(t,"b",(function(){return l})),n.d(t,"a",(function(){return c})),n.d(t,"g",(function(){return d})),n.d(t,"c",(function(){return u}));const{version:o,name:i}=n(84),r=i,s=o,a={MOVIE:"MOVIE",CHAPTER:"CHAPTER"},l=.95*Math.PI*2,c=10,d=240,u={DATA_LOADED:"DATA_LOADED",SELECT_COLOR_MODE:"SELECT_COLOR_MODE",SELECT_PRESET:"SELECT_PRESET",SELECT_MOVIES:"SELECT_MOVIES"}},10:function(e,t,n){"use strict";n.d(t,"a",(function(){return i})),n.d(t,"b",(function(){return r})),n.d(t,"d",(function(){return s})),n.d(t,"c",(function(){return a}));var o=n(1);const i=e=>t=>{t({type:o.c.DATA_LOADED,data:e})},r=e=>t=>{t({type:o.c.SELECT_COLOR_MODE,colorMode:e})},s=e=>(t,n)=>{const o=n().presets[e];t(a(o))},a=e=>t=>{const n=e.map(e=>encodeURIComponent(e)).join(","),i=new URL(window.location.href.split("#/")[0]),r=`${i.protocol}//${i.host}${i.pathname}?selection=${n}`;history.replaceState({},null,r),t({type:o.c.SELECT_MOVIES,movies:e})}},15:function(e,t,n){"use strict";n.d(t,"c",(function(){return p})),n.d(t,"d",(function(){return f})),n.d(t,"e",(function(){return v})),n.d(t,"a",(function(){return g})),n.d(t,"b",(function(){return b}));var o=n(32),i=n.n(o),r=n(24),s=n.n(r),a=n(31),l=n.n(a),c=n(6),d=n(30),u=n.n(d),m=n(1);function p(e){let t=0;const n=s()(1,(e.chaptercolors||[]).length).map(n=>{const o=e.chapters[n-1],i=e.chapters[n],r=i-o,s=m.b*(r/e.movie.duration);t+=s;const a=e.chaptercolors[n-1].map(e=>({fraction:e["%"],rgb:{r:e.rgb[0]/255,g:e.rgb[1]/255,b:e.rgb[2]/255}})).filter(e=>null!==e.fraction).map(e=>(e.fraction*=2.5,e));return{startframe:o,endframe:i,duration:r,angle:t,colors:a}});n.length||console.warn(e.title,"missing chapter info");const o=function(e,t){const n=Math.round(e.length/t),o=e.length/n,i=s()(0,n).map(()=>[]);return e.forEach((e,t)=>{const n=Math.floor(t/o);i[n].push(e)}),i}(e.shots,m.a);let r=0,a=o.map(t=>{const n=l()(t.map(i()("duration"))),o=3.5*(s=t.map(i()("motion")),l()(s)/s.length);var s;const a=m.b*(n/e.movie.duration);return r+=a,{duration:n,motion:o,angle:r}});const c=e.movie.colors.map(e=>({fraction:e["%"],rgb:{r:e.rgb[0]/255,g:e.rgb[1]/255,b:e.rgb[2]/255}}));if(n.length){let e=0;a=a.map(t=>{const o=n[e].angle;return t.angle>o&&e++,e>n.length-1&&(e=n.length-1),t.chapterIndex=e,t})}return{title:e.title,movieColors:c,segments:a,chapters:n}}const h=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];function f(e,t,n){const o=e.segments,i=new c.b,r=[],a=[],l=[];return o.forEach((i,c)=>{const d=0===c?0:o[c-1].angle,p=i.angle,f=(n||t)===m.f.CHAPTER&&e.chapters.length&&e.chapters[i.chapterIndex]?e.chapters[i.chapterIndex].colors:e.movieColors;let v=0;const g=Math.sin(d),b=Math.cos(d),E=Math.sin(p),y=Math.cos(p);f.forEach(e=>{let{fraction:t,rgb:n}=e;const o=u()(v,0,1);v+=t;const c=u()(v,0,1),d=[g,b,c,i.motion],m=[E,y,c,i.motion],p=[E,y,o,i.motion],f=[g,b,o,i.motion];r.push(...d,...m,...f,...f,...m,...p),a.push(...h),s()(0,h.length/3).forEach(()=>{l.push(n.r,n.g,n.b)})})}),i.setAttribute("position",new c.a(new Float32Array(a),3)),i.setAttribute("color",new c.a(new Float32Array(l),3)),i.setAttribute("sinCosOffsetMotion",new c.a(new Float32Array(r),4)),i}function v(e,t){const n={time:{type:"f",value:0},halfThickness:{type:"f",value:t.halfThickness},radius:{type:"f",value:t.radius},amplitude:{type:"f",value:t.amplitude},horizontalOffset:{type:"f",value:t.horizontalOffset}};return new c.g({uniforms:n,vertexShader:e.vertex,fragmentShader:e.fragment,vertexColors:c.c})}function g(e,t){const n=t/9e4/2,o=function(e){return.25*e}(e),i=Math.sqrt(n*(o*o)),r=function(e){return.7*e}(o),s=.5*r,a=function(e,t,n){return e/2-t-n/2}(e,o,r);return{radius:i,thickness:r,halfThickness:s,maxAmplitude:a,amplitude:function(e){return.4*e}(a)}}function b(e){for(;e.children.length>0;){const t=e.children[0];t.geometry&&t.geometry.dispose(),t.material&&t.material.dispose(),e.remove(t)}}},23:function(e,t,n){"use strict";t.a=n.p+"assets/x.2aab64bf773074efe8d933dad3d74586.svg"},29:function(e,t,n){"use strict";n.d(t,"b",(function(){return i}));var o=n(1);const i={movies:void 0,presets:void 0,selectedMovies:[],selectedPreset:void 0,colorMode:o.f.MOVIE};t.a=function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:i,t=arguments.length>1?arguments[1]:void 0;return t.type===o.c.DATA_LOADED?{...e,movies:t.data.movies,presets:t.data.presets}:t.type===o.c.SELECT_COLOR_MODE?{...e,colorMode:t.colorMode}:t.type===o.c.SELECT_MOVIES?{...e,selectedMovies:t.movies}:e}},34:function(e,t,n){"use strict";n.d(t,"a",(function(){return i})),n.d(t,"b",(function(){return r}));var o=n(1);const i=()=>{console.log(`${o.d} ${o.e}`),console.log("NODE_ENV: production"),console.log("URL_PREFIX: /")},r=e=>e[Math.floor(Math.random()*e.length)]},50:function(e,t,n){"use strict";n.d(t,"a",(function(){return r}));var o=n(13),i=n.n(o);function r(){return fetch("data/movies.json").then(e=>e.json()).then(e=>{const t=i()(e.movies).map(t=>{const n="data/"+e.movies[t];return fetch(n).then(e=>e.json()).then(e=>({name:t,data:e}))});return Promise.all(t).then(t=>{const n={...e};return t.forEach(e=>{let{name:t,data:o}=e;n.movies[t]=o}),n})})}},51:function(e,t,n){"use strict";(function(e,o,i){var r=n(14),s=n(3),a=n(52),l=n(60),c=n(64),d=n(66),u=n(1);const m=e.createElement("div",{className:o`
		position: fixed;
		background: rgb(215, 215, 215);
		z-index: 9999;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	`},"Loading...");class p extends e.PureComponent{render(){const{dispatch:t,movies:n,presets:i,colorMode:p,selectedMovies:h}=this.props;return e.createElement("div",{id:"app-inner"},e.createElement(r.a,{basename:"/"},n&&i?[e.createElement(a.a,{dispatch:t,movies:n,selectedMovies:h,key:"0"}),e.createElement(l.a,{colorMode:p,movies:h.map(e=>n[e]),key:"1"}),e.createElement(c.a,{dispatch:t,colorMode:p,presets:i,key:"2"}),e.createElement("div",{id:"still",className:o`width: ${u.g}px;`,key:"3"},e.createElement("img",{id:"still-image",src:"",className:o`
									width: ${u.g}px;
									margin-left: -${u.g}px;
								`}))]:m,e.createElement(s.a,{path:"/info",render:()=>e.createElement("div",{className:o`
								position: fixed;
								background: rgba(255, 255, 255, 0.9);
								z-index: 10000;
								top: 0;
								left: 0;
								width: 100%;
								height: 100%;
								overflow-y: auto;
								display: flex;
								flex-direction: column;
								align-items: center;
								padding: 1rem;
							`},e.createElement(d.a,null))})))}}p.propTypes={dispatch:i.func.isRequired,movies:i.object,presets:i.object,colorMode:i.string.isRequired,selectedMovies:i.array.isRequired},p.defaultProps={movies:null,presets:null},t.a=p}).call(this,n(0),n(17).css,n(11))},52:function(e,t,n){"use strict";(function(e,o,i,r){var s=n(59),a=n.n(s),l=n(58),c=n.n(l),d=n(53),u=n(10),m=n(23),p=n(57);const h=e`
	position: fixed;
	top: 0;
	padding: 1rem;
`,f=function(t,n){let i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"left";return o.createElement("div",{key:i,className:e`
			${h};
			${i}: 0;
			z-index: 100;
			cursor: pointer;
		`},o.createElement("div",{onClick:()=>{t(Object(u.c)("left"===i?["",...n]:[...n,""]))}},o.createElement("img",{src:p.a,alt:"add movie"})))},v=t=>{let{dispatch:n,movies:r,selectedMovies:s}=t;return o.createElement(i,null,f(n,s,"left"),f(n,s,"right"),o.createElement("div",{className:e`
				${h};
				left: 0;
				z-index: 99;
				width: 100%;
				display: flex;
				justify-content: space-around;
			`},s.map((t,i)=>{const l=r[t];return o.createElement("div",{key:""===t?i:t},o.createElement("div",{className:e`
							display: flex;
							align-items: center;
						`},o.createElement(d.a,{selection:t,selectedMovies:s,movies:r,changeHandler:e=>{n(Object(u.c)(c()(i,e,s)))}}),o.createElement("div",{disabled:1===s.length,onClick:()=>{n(Object(u.c)(a()(i,1,s)))},className:e`
								cursor: pointer;
								display: block;
								height: 14px;
								margin-left: 3px;
							`},o.createElement("img",{src:m.a,alt:"remove"}))),l?o.createElement("div",{className:e`
								text-align: center;
								font-size: 12px;
								margin-top: 3px;
							`},l.director,o.createElement("br",null),l.year):null)})))};v.propTypes={dispatch:r.func.isRequired,movies:r.object.isRequired,selectedMovies:r.array.isRequired},v.defaultProps={},t.a=v}).call(this,n(17).css,n(0),n(0).Fragment,n(11))},53:function(e,t,n){"use strict";(function(e,o){var i=n(56),r=n.n(i),s=n(22),a=n.n(s),l=n(55),c=n.n(l),d=n(13),u=n.n(d),m=n(54),p=n.n(m);const h=t=>{const{movies:n,selection:o,changeHandler:i,selectedMovies:s}=t,l=p()(u.a,c()(a.a))(n);return e.createElement("select",{value:o,onChange:e=>{i(e.target.value)}},e.createElement("option",{value:""}),l.map(t=>e.createElement("option",{key:t,value:t,disabled:r()(t,s)},t)))};h.propTypes={movies:o.object.isRequired,selection:o.string.isRequired,selectedMovies:o.array.isRequired,changeHandler:o.func.isRequired},h.defaultProps={},t.a=h}).call(this,n(0),n(11))},57:function(e,t,n){"use strict";t.a=n.p+"assets/+.5532b2f9139dc1320893969d0e0fe900.svg"},60:function(e,t,n){"use strict";(function(e,o,i,r){var s=n(28),a=n.n(s),l=n(63),c=n.n(l),d=n(6),u=n(61),m=n.n(u),p=n(62),h=n(69),f=n(15),v=n(1);const g=e`
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
`,b={antialias:!0,alpha:!0},E=e=>Math.min(.9*window.innerHeight,e),y=(e,t)=>(e+1)*t-.5*t,w=e=>window.innerWidth/e,x=()=>{document.querySelector("#still").style.display="none"};class M extends o.Component{constructor(e){super(e);let t=0;this.start=function(){this.frameId||(this.frameId=requestAnimationFrame(this.update))}.bind(this),this.stop=function(){cancelAnimationFrame(this.frameId)}.bind(this),this.update=function(){this.frameId=window.requestAnimationFrame(this.update),t++,this.scene.children.forEach(e=>{e.material.uniforms.time.value=.15*t,e.material.uniforms.time.needsUpdate=!0}),this.renderer.render(this.scene,this.camera)}.bind(this),this.updateData=this.updateData.bind(this),this.handleMouseMove=this.handleMouseMove.bind(this),this.handleMouseDown=this.handleMouseDown.bind(this),this.handleMouseUp=this.handleMouseUp.bind(this)}componentDidMount(){const e=this.mount.clientWidth,t=this.mount.clientHeight;this.scene=new d.f,this.camera=new d.e(-.5*e,.5*e,.5*t,-.5*t,0,1),this.camera.position.z=0,this.renderer=new d.i(b),this.renderer.setPixelRatio(window.devicePixelRatio),this.renderer.setSize(e,t),this.renderer.domElement.id="canvas",this.mount.appendChild(this.renderer.domElement),this.updateData(this.props.movies,this.props.colorMode)}componentWillUnmount(){this.stop(),this.controls.dispose(),this.mount.removeChild(this.renderer.domElement)}UNSAFE_componentWillReceiveProps(e){this.updateData(e.movies,e.colorMode)}updateData(e,t){Object(f.b)(this.scene);const n=w(e.length);this._centers=e.map((e,o)=>{if(!e)return;const i=Object(f.c)(e),r=Object(f.d)(i,t),s=Object(f.a)(E(n),e.movie.duration),a=y(o,n),l=window.innerHeight/2;s.horizontalOffset=a-.5*window.innerWidth;const c=Object(f.e)(h.a,s),u=new d.d(r,c);return this.scene.add(u),new d.h(a,l)}),this.start()}handleMouseMove(e){const[t,n]=[e.clientX,e.clientY];let o=-1,i=1/0;this._centers.forEach((e,n)=>{if(!e)return;const r=Math.abs(t-e.x);r<i&&(i=r,o=n)});const{movies:r}=this.props,s=r[o],a=new d.h(t,n),l=this._centers[o];if(l.distanceTo(a)>.4*w(r.length))return this.renderer.domElement.style.cursor="default",void x();if(s.stills&&(this.renderer.domElement.style.cursor="zoom-in"),!this.mouseDown||!s.stills)return void x();const c=a.sub(l);let u=Math.atan2(c.x,-c.y);if(u<0&&(u+=2*Math.PI),u>v.b)return void x();const p=s.stills.length,h=m()(u,0,v.b,0,1),f=Math.floor(p*h);((e,t,n,o)=>{const i=document.querySelector("#still-image");i.src=e,i.height=o;const r=i.parentElement;r.style.top=n+"px";const s=t-v.g>0?t:t+Math.min(v.g-t,v.g);r.style.left=s+"px",r.style.display="block"})(((e,t)=>`data/movies/${t}/stills/${e}`)(s.stills[f],s.title),t,n,s.height)}handleMouseDown(e){e.stopPropagation(),this.mouseDown=!0}handleMouseUp(e){e.stopPropagation(),this.mouseDown=!1}render(){const{movies:t}=this.props,n=c()(a()(void 0))(t);let r,s;return n>=0&&(s=w(t.length),r=y(n,s)),o.createElement(i,null,o.createElement("div",{className:g,ref:e=>{this.mount=e},onMouseDown:this.handleMouseDown,onMouseUp:this.handleMouseUp,onMouseMove:this.handleMouseMove}),r?o.createElement("img",{src:p.a,alt:"legend",className:e`
						pointer-events: none;
						z-index: 99;
						position: fixed;
						top: 50%;
						left: ${r}px;
						width: ${E(s)}px;
						transform: translateY(-50%) translateX(-50%);
					`}):null)}}M.propTypes={movies:r.array,colorMode:r.string.isRequired},M.defaultProps={movies:[]},t.a=M}).call(this,n(17).css,n(0),n(0).Fragment,n(11))},62:function(e,t,n){"use strict";t.a=n.p+"assets/legend.19dfbec8eb2c2ec27562d70ecaaffb77.svg"},64:function(e,t,n){"use strict";(function(e,o,i){var r=n(14),s=n(1),a=n(10);const l=e`
	display: flex;
	align-items: center;
`,c=e`
	position: fixed;
	bottom: 0;
	padding: 1rem;
`,d=t=>{const{dispatch:n,presets:i,colorMode:d}=t;return o.createElement("div",{className:e`
			z-index: 99;
			user-select: none;
		`},o.createElement("div",{className:e`
				${c};
				left: 0;
			`},o.createElement(r.b,{to:"info"},"Info")),o.createElement("div",{className:e`
				${c};
				left: 50%;
				transform: translateX(-50%);
				display: flex;
			`},o.createElement("div",{className:e`
					display: flex;
					margin-right: 3rem;
				`},o.createElement("div",{className:e`margin-right: 1rem;`},"Options:"),o.createElement("div",null,o.createElement("div",{className:l},o.createElement("input",{type:"checkbox",id:"colors-checkbox-movie",checked:d===s.f.MOVIE,onChange:e=>{e.target.checked&&n(Object(a.b)(s.f.MOVIE))}}),o.createElement("label",{htmlFor:"colors-checkbox-movie"},"Movie colors")),o.createElement("div",{className:l},o.createElement("input",{type:"checkbox",id:"colors-checkbox-chapters",checked:d===s.f.CHAPTER,onChange:e=>{e.target.checked&&n(Object(a.b)(s.f.CHAPTER))}}),o.createElement("label",{htmlFor:"colors-checkbox-chapters"},"Chapter colors")))),o.createElement("div",null,o.createElement("div",{className:e`
						display: inline-block;
						margin-right: 1rem;
					`},"Presets:"),o.createElement("select",{value:"",onChange:e=>{n(Object(a.d)(e.target.value))}},o.createElement("option",{value:"",disabled:!0}),Object.keys(i).map(e=>o.createElement("option",{key:e,value:e},e))))))};d.propTypes={dispatch:i.func.isRequired,colorMode:i.string.isRequired,presets:i.object.isRequired},d.defaultProps={},t.a=d}).call(this,n(17).css,n(0),n(11))},66:function(e,t,n){"use strict";(function(e,o,i){var r=n(14),s=n(23);t.a=()=>e.createElement(o,null,e.createElement("div",{className:i`
			position: fixed;
			top: 0;
			right: 0;
			padding: 1rem;
			padding-right: 2rem;
		`},e.createElement(r.b,{to:"/"},e.createElement("img",{src:s.a,alt:"close",style:{width:32}}))),e.createElement("div",{className:i`width: 100%; max-width: 1400px;`},e.createElement("div",{className:i`
				position: relative;
				padding-top: 56.25%;
				width: 100%;
			`},e.createElement("iframe",{src:"https://player.vimeo.com/video/26584083?title=0&byline=0&portrait=0&color=2cbad2",width:"960",height:"450",frameBorder:"0",className:i`
					position: absolute;
					top: 0;
					left: 0;
					width: 100%;
					height: 100%;
				`}))),e.createElement("div",{className:i`
			max-width: 40em;
			font-size: 24px;
			line-height: 1.25;
			display: flex;
			flex-direction: column;
		    align-items: stretch;
			> * {
				display: block;
			}
		`},e.createElement("p",null,e.createElement("br",null),"Created by: ",e.createElement("a",{href:"http://www.freder.io/",target:"_blank"},"Frederic Brodbeck")),e.createElement("p",null,"Cinemetrics is a tool for measuring and visualizing movie data, in order to reveal the characteristics of films and to create visual “fingerprints” of them. Information such as the editing structure, color, speech or motion are extracted, analyzed and transformed into graphic representations, that can be easily interpreted or compared side by side."),e.createElement("p",null,"Since film / video is a time-based medium, it can only be seen one image at a time – that’s why it’s hard to capture and display them in their entirety. There are a lot of information graphics based on metadata related to film and cinema (budget, box office data, awards won, relationship between characters, etc.). This project on the other hand concentrates on the movie itself, examining the formal and structural characteristics. This turns out to be especially interesting, when looking at two or more movies next to each other and to be able to immediately see the similarities and differences. For example:"),e.createElement("ul",null,e.createElement("li",null,"Original vs. remake"),e.createElement("li",null,"Movies of the same genre / series"),e.createElement("li",null,"Different epochs of film-making"),e.createElement("li",null,"Movies by one director")),e.createElement("p",null,"Cinemetrics is an experimental exploration of the data that is inherent in a movie, visualizing some of the aspects that would otherwise remain unseen. The workflow looks like this:"),e.createElement("div",{className:i`
			align-self: center;
			border-radius: 300px;
    		overflow: hidden;
			padding: 60px;
			background: white;
			img { display: block; }
		`},e.createElement("img",{src:"assets/schema_web.png"})),e.createElement("p",null,"Part of the project are custom pieces of software – tools for disassembling video files into their components (video, audio, subtitles, etc.) and processing them (shot detection, average shot length, motion measuring, color palettes), as well as an interactive application to generate and visualize different movie fingerprints. Some of the code ",e.createElement("a",{href:"https://github.com/freder/cinemetrics/"},"is available here"),".")))}).call(this,n(0),n(0).Fragment,n(17).css)},69:function(e,t,n){"use strict";t.a={vertex:"// provided by three.js\n// attribute vec3 color;\n// ...\n\nuniform float time;\nuniform float radius;\nuniform float halfThickness;\nuniform float amplitude;\nuniform float horizontalOffset;\n\nattribute vec4 sinCosOffsetMotion;\n\nvarying vec3 vColor;\n\n\n// replacement for sin() -- slightly more interesting motion\n// 1.25*(sin(x)-sin^3(x)/5)\n// http://www.wolframalpha.com/input/?i=1.25*%28sin%28x%29-sin^3%28x%29%2F5%29+vs+sin%28x%29\nfloat oscillate(float a) {\n\tfloat s = sin(a);\n\treturn 1.25 * (s - (pow(s, 3.0) / 5.0));\n}\n\nvoid main() {\n\tfloat sine = sinCosOffsetMotion.r;\n\tfloat cosine = sinCosOffsetMotion.g;\n\tfloat offset = sinCosOffsetMotion.b;\n\tfloat motion = sinCosOffsetMotion.a;\n\n\tfloat amp = motion * amplitude;\n\tfloat motionOffset = amp * sin(time * motion);\n\tfloat r = radius + motionOffset;\n\tfloat offsetRadius = r + mix(halfThickness, -halfThickness, offset);\n\tvec2 pos = vec2(\n\t\toffsetRadius * sine + horizontalOffset,\n\t\toffsetRadius * cosine\n\t);\n\n\tvColor = color;\n\tgl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 0.0, 1.0);\n}\n",fragment:"varying vec3 vColor;\n\nvoid main() {\n\tgl_FragColor = vec4(vColor, 1.0);\n}\n"}},70:function(e,t,n){e.exports=n(71)},71:function(e,t,n){"use strict";n.r(t),function(e){var t=n(68),o=n.n(t),i=n(13),r=n.n(i),s=n(22),a=n.n(s),l=n(47),c=n.n(l),d=n(21),u=n.n(d),m=n(35),p=n(36),h=n(67),f=n(49),v=n(10),g=n(29),b=n(50),E=n(51),y=n(34);Object(y.a)();const w=Object(f.createLogger)({collapsed:!0,timestamp:!1}),x=Object(p.b)(g.a,g.b,Object(p.a)(h.a,w)),M=Object(m.b)(a.a)(E.a);u.a.render(e.createElement(m.a,{store:x},e.createElement(M,null)),document.getElementById("app")),Object(b.a)().then(e=>{x.dispatch(Object(v.a)(e));const t=new URL(window.location.href.split("#/")[0]),n=c.a.parse(t.search);if(n.selection){const e=n.selection.split(",").map(e=>decodeURIComponent(e));x.dispatch(Object(v.c)(e))}else{const t=r()(e.movies),n=o()(e.presets.Archetypes,t),i=[Object(y.b)(n),""];x.dispatch(Object(v.c)(i))}})}.call(this,n(0))},84:function(e){e.exports=JSON.parse('{"name":"cinemetrics.site","version":"0.0.0","browserslist":"last 2 versions, not dead, >1%, not ie > 0","scripts":{"dev":"NODE_ENV=development npx webpack-dev-server --host \'0.0.0.0\' --content-base ./src --mode development","build:staging":"rm -rf build ; NODE_ENV=production URL_PREFIX=\'/build/\' npx webpack --mode production ; rm build/*.map","build":"rm -rf build ; NODE_ENV=production URL_PREFIX=\'/\' npx webpack --mode production ; rm build/*.map","serve":"serve build","test":"NODE_ENV=test jest","lint":"npx eslint --report-unused-disable-directives __tests__ src"},"dependencies":{"@emotion/core":"^10.0.27","@emotion/styled":"^10.0.27","emotion":"^10.0.27","mout":"^1.2.2","prop-types":"^15.7.2","query-string":"^6.11.0","ramda":"^0.27.0","react":"^16.12.0","react-color":"^2.18.0","react-dom":"^16.12.0","react-redux":"^7.2.0","react-router-dom":"^5.1.2","redux":"^4.0.5","redux-logger":"^3.0.6","redux-thunk":"^2.3.0","three":"^0.113.2"},"devDependencies":{"@babel/core":"^7.2.0","@babel/preset-env":"^7.8.4","@babel/preset-react":"^7.8.3","babel-eslint":"^10.0.1","babel-loader":"^8.0.4","babel-plugin-emotion":"^10.0.5","babel-plugin-jsx-control-statements":"^4.0.0","babel-plugin-ramda":"^2.0.0","copy-webpack-plugin":"^5.0.4","eslint":"^6.1.0","eslint-plugin-jest":"^23.7.0","eslint-plugin-jsx-control-statements":"^2.2.1","eslint-plugin-react":"^7.18.3","file-loader":"^5.1.0","jest":"^25.1.0","raw-loader":"^4.0.0","webpack":"^4.41.6","webpack-cli":"^3.3.11","webpack-dev-server":"^3.10.3"}}')}});
//# sourceMappingURL=main.js.map