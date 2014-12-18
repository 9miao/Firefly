#Firefly
=======

####firefly 分支gfirefly介绍

firefly-gevent 是firefly的gevent版本。相比现在的firefly版本使用的twisted，gevent更加的精简。<br/>
firefly-gevent结合了gevent的性能，封装了网络IO处理、数据库IO读写缓存、分布式进程间接口调用。这样使得游戏服务端的开发变得更加的轻松简单，开发者不必在面对这些的技术难题，专心致力于游戏玩法逻辑的开发。<br/>
省略了远程调用过程中添加回调函数callback的步骤。<br/>
你可以这样去写远程调用的方法<br/>


	result = root.callChild("test_node",1,u'Root测试')
	#这里不会阻塞的,在结果返回之前会执行别的协程
	print result
	#当结果返回的时候会继续往下执行

gfirefly开源地址:https://github.com/9miao/G-Firefly<br/>
gtwisted开源地址:https://github.com/9miao/gtwisted<br/>

<body class="single single-post postid-31 single-format-standard custom-background single-author singular two-column right-sidebar">
Home Page: <a href="http://www.9miao.com">http://9miao.com<a>
<div id="page" class="hfeed">


	<div id="main">

		<div id="primary">
			<div id="content" role="main">
					
<article id="post-31" class="post-31 post type-post status-publish format-standard hentry category-firefly">
	<header class="entry-header">
		<h1 class="entry-title">Firefly Game Server Framework Intro</h1>

			</header>

	<div class="entry-content">
		<p align="left">Firefly, written in Python and based on Twisted framework development, is a distributed game server framework with free, open source, stable, rapid extension and hot update features. With development framework, database caching and other basic game server services encapsulating, it signicantly reduces game development working time thereby truely allowing its users to spend more time on gameplay logic implementation. It also can be used to build customized distributed framwork, and only having a corresponding configuration file modification demand.</p>
<p align="left"><strong>Advantages and Features</strong><b></b></p>
<ul>
<li>Single-threaded and multi-porcess architecture with customized distributed architecture support</li>
<li>Conveninent server extension mechanism that can rapidly extend server type and quantity</li>
<li>TCP persistent connections to clients without issues like stick pack concerns</li>
<li>data caching services encapsulating</li>
<li>real-time hot updating data and game logic with no disturbing on client players</li>
<li>dozens of basic gameplay system modules for assembly using (V1. 3. 0 available)</li>
</ul>
<p align="left"><strong>Framework Description</strong></p>
<p align="left"><a href="http://9miao.com"><img class="alignnone  wp-image-40" alt="123" src="http://firefly2.9miao.com/wp-content/uploads/2013/08/123.jpg" width="601" height="441"></a></p>
<ul>
<li>Management: Firefly is a multi-process distributed game server, thererfore the management and extension of all game servers (processes) is a crucial part of Firefly, and extending servers will be very easy through framework.</li>
<li>Network: the skeleton of game framework is constituted by client connections communications, server inter-process communication and others, and all game flow is based on this context. Server’s communication with clients adopts request-reply mode, it will give corresponding response by all received client’s request, and can also active push and broadcast information to clients. All these requests are based on instructions number (such as difining 101 as login instruction). Here the inter-server process communication adopts asynchronous callback mode, thus reducing the time cost of inter-process communication through networks.</li>
<li>Data: data processing is a significant part of online game in which mass data needs to be stored and updated, thus the database’s read-write rate becomes the biggest performance bottleneck of server. Firefly’s db processing is able to cache the data from database table to memcache, and operate data by calling corresponding object method in the form of object, obtain synchronous data by instantiating cache instances with same name in different process and wirte the cache object’s data back to database.</li>
</ul>
<p align="left"><strong>Framework Ideas</strong><b></b></p>
<p align="left"><b>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</b>the most basic server is a continually running application. In a distributed game server, the features we need includes: monitoring client connections and other service processes’ message as well as connecting these service processes, and sometimes database connections and caching services are also required. It’s shown below:</p>
<p align="left">&nbsp;<a href="http://9miao.com/"><img class="alignnone size-full wp-image-41" alt="234" src="http://firefly2.9miao.com/wp-content/uploads/2013/08/234.jpg" width="552" height="401"></a></p>
<p align="left">Net connect works as client connection, root monitors other server processes’ message, and node connects other server processes, db database and caches. whether to monitor client connections and other service processes’ message as well as each server’s name and their connection relationship are all can be configured in config.json, thus developers could get their own customized distributed framework.</p>
			</div>

</article>

				
			</div>
		</div>


	</div>

</div>

</body>
