<div align="center">
  <img src="img/luffy.gif" width="180" alt="Luffy" />
</div>

<br />

```aura width=800 height=180
<div style={{
  width: 800, height: 180, position: 'relative', display: 'flex'
}}>
  <div style={{
    position: 'absolute', top: 0, left: 0, width: 800, height: 180,
    borderRadius: 16, background: 'linear-gradient(135deg, #0c0d14 0%, #070709 100%)',
    border: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', alignItems: 'center', paddingLeft: 40, paddingRight: 40
  }}>
    <div style={{
      width: 100, height: 100, borderRadius: 50,
      background: 'linear-gradient(135deg, #8f43ee, #00c4ff)',
      display: 'flex', alignItems: 'center', justifyContent: 'center'
    }}>
      <img src={github?.user?.avatarUrl ?? 'https://github.com/Gerryrag.png'} width={92} height={92} style={{ borderRadius: 46 }} />
    </div>

    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: 30, flex: 1 }}>
      <span style={{ fontFamily: 'Arial', fontWeight: 800, fontSize: 32, color: '#ffffff', marginBottom: 4 }}>
        Gerry Robbie AG
      </span>
      
      <span style={{ fontFamily: 'Arial', fontSize: 15, color: 'rgba(255, 255, 255, 0.6)', marginBottom: 12 }}>
        Information Systems Student @ Unmer | Web Developer &amp; Video Editor
      </span>
      
      <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
        {['HTML5', 'CSS3', 'PHP', 'Laravel', 'Photoshop'].map((skill) => (
          <div key={skill} style={{
            display: 'flex', padding: '4px 14px', borderRadius: 20,
            background: 'rgba(143, 67, 238, 0.08)', border: '1px solid rgba(143, 67, 238, 0.3)',
            color: 'rgba(205, 195, 255, 0.85)', fontSize: 12, fontWeight: 600
          }}>
            {skill}
          </div>
        ))}
      </div>
    </div>
  </div>
</div>
```

<br />

```aura width=800 height=160
<div style={{
  width: 800, height: 160, position: 'relative', display: 'flex'
}}>
  <div style={{
    position: 'absolute', top: 0, left: 0, width: 800, height: 160,
    borderRadius: 16, background: 'linear-gradient(135deg, #0c0d14 0%, #070709 100%)',
    border: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', alignItems: 'center',
    justifyContent: 'space-around', paddingLeft: 40, paddingRight: 40
  }}>
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1 }}>
      <span style={{ fontFamily: 'Arial', fontWeight: 900, fontSize: 36, color: '#bc7af9', marginBottom: 6 }}>
        {github?.stats?.totalRepos ?? 0}
      </span>
      <span style={{ fontFamily: 'Arial', fontWeight: 'bold', fontSize: 12, color: 'rgba(255, 255, 255, 0.4)', letterSpacing: '1px' }}>
        REPOS
      </span>
    </div>
    
    <div style={{ width: 1, height: 60, backgroundColor: 'rgba(255, 255, 255, 0.08)', display: 'flex' }} />

    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1 }}>
      <span style={{ fontFamily: 'Arial', fontWeight: 900, fontSize: 36, color: '#4d96ff', marginBottom: 6 }}>
        {github?.stats?.totalStars ?? 0}
      </span>
      <span style={{ fontFamily: 'Arial', fontWeight: 'bold', fontSize: 12, color: 'rgba(255, 255, 255, 0.4)', letterSpacing: '1px' }}>
        STARS
      </span>
    </div>
    
    <div style={{ width: 1, height: 60, backgroundColor: 'rgba(255, 255, 255, 0.08)', display: 'flex' }} />

    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1 }}>
      <span style={{ fontFamily: 'Arial', fontWeight: 900, fontSize: 36, color: '#ff8e2b', marginBottom: 6 }}>
        {github?.stats?.totalCommits ?? 0}
      </span>
      <span style={{ fontFamily: 'Arial', fontWeight: 'bold', fontSize: 12, color: 'rgba(255, 255, 255, 0.4)', letterSpacing: '1px' }}>
        COMMITS
      </span>
    </div>
  </div>
</div>
```

<br />

```aura width=800 height=180
<div style={{
  width: 800, height: 180, position: 'relative', display: 'flex'
}}>
  <div style={{
    position: 'absolute', top: 0, left: 0, width: 800, height: 180,
    borderRadius: 16, background: 'linear-gradient(135deg, #0c0d14 0%, #070709 100%)',
    border: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', flexDirection: 'column',
    padding: 30
  }}>
    <span style={{ fontFamily: 'Arial', fontWeight: 'bold', fontSize: 11, color: 'rgba(255, 255, 255, 0.4)', letterSpacing: '1.5px', marginBottom: 20 }}>
      TECH STACK
    </span>
    
    <div style={{ display: 'flex', alignItems: 'center', marginBottom: 15 }}>
      <span style={{ fontFamily: 'Arial', fontWeight: 'bold', fontSize: 12, color: '#bc7af9', width: 120, letterSpacing: '0.5px' }}>
        LANGUAGES
      </span>
      <div style={{ display: 'flex', gap: 8 }}>
        {['PHP', 'JavaScript', 'HTML5', 'CSS3'].map((lang) => (
          <div key={lang} style={{
            display: 'flex', padding: '4px 14px', borderRadius: 20,
            background: 'rgba(255, 255, 255, 0.04)', border: '1px solid rgba(255, 255, 255, 0.1)',
            color: '#ffffff', fontSize: 12, fontWeight: 600
          }}>
            {lang}
          </div>
        ))}
      </div>
    </div>
    
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <span style={{ fontFamily: 'Arial', fontWeight: 'bold', fontSize: 12, color: '#4d96ff', width: 120, letterSpacing: '0.5px' }}>
        TOOLS &amp; LIBS
      </span>
      <div style={{ display: 'flex', gap: 8 }}>
        {['Laravel', 'Bootstrap', 'Photoshop'].map((tool) => (
          <div key={tool} style={{
            display: 'flex', padding: '4px 14px', borderRadius: 20,
            background: 'rgba(255, 255, 255, 0.04)', border: '1px solid rgba(255, 255, 255, 0.1)',
            color: '#ffffff', fontSize: 12, fontWeight: 600
          }}>
            {tool}
          </div>
        ))}
      </div>
    </div>
  </div>
</div>
```

<br />
<br />

<div align="center">
  <a href="https://www.linkedin.com/in/gerryrag" target="_blank">
    <img src="img/badge_linkedin.svg" alt="LinkedIn" height="36" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.youtube.com/@Gerryrag" target="_blank">
    <img src="img/badge_youtube.svg" alt="YouTube" height="36" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.instagram.com/gerryrag" target="_blank">
    <img src="img/badge_instagram.svg" alt="Instagram" height="36" />
  </a>
</div>
