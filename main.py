import logging,time,uuid
from fastapi import FastAPI,Query,Request
from fastapi.middleware.cors import CORSMiddleware
from .models import Capability,Metadata,Person
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s');log=logging.getLogger('directory-api')
app=FastAPI(title='Capability Team Directory API',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['http://localhost:5173'],allow_methods=['GET'],allow_headers=['*'])
PEOPLE=[
Person(id=1,name='Maya Chen',role='Senior Software Engineer',team='AI Platform',location='New York, NY',skills=['Python','React','TypeScript','FastAPI'],capabilities=[Capability(name='Model Serving',category='AI Platform',maturity=4),Capability(name='Knowledge Retrieval',category='AI Platform',maturity=4),Capability(name='Observability',category='Platform',maturity=3)],summary='Builds internal AI platform services and product-facing integrations.'),
Person(id=2,name='Jordan Patel',role='Frontend Engineer',team='Enterprise Experience',location='Phoenix, AZ',skills=['React','TypeScript','Accessibility','Vitest'],capabilities=[Capability(name='Capability Exploration',category='Experience',maturity=5),Capability(name='Search & Filtering',category='Experience',maturity=4),Capability(name='Design Systems',category='Experience',maturity=4)],summary='Focuses on data-heavy React experiences and accessible internal tooling.'),
Person(id=3,name='Elena Garcia',role='ML Engineer',team='Risk Intelligence',location='Concord, CA',skills=['Python','XGBoost','Spark','MLflow'],capabilities=[Capability(name='Feature Engineering',category='ML',maturity=5),Capability(name='Model Operations',category='ML',maturity=4),Capability(name='Batch Scoring',category='Data',maturity=4)],summary='Operationalizes predictive models and large-scale feature pipelines.'),
Person(id=4,name='Noah Williams',role='Platform Engineer',team='Core Platform',location='Charlotte, NC',skills=['Kubernetes','Docker','Python','AWS'],capabilities=[Capability(name='Container Platform',category='Platform',maturity=5),Capability(name='Deployment Automation',category='Platform',maturity=4),Capability(name='Service Reliability',category='Platform',maturity=5)],summary='Owns reusable deployment patterns and production reliability standards.'),
Person(id=5,name='Priya Raman',role='Data Engineer',team='Knowledge Systems',location='Dallas, TX',skills=['Python','Spark','Airflow','SQL'],capabilities=[Capability(name='Taxonomy Ingestion',category='Knowledge',maturity=4),Capability(name='Data Normalization',category='Knowledge',maturity=5),Capability(name='Pipeline Orchestration',category='Data',maturity=4)],summary='Builds pipelines that normalize enterprise data for discovery experiences.'),
Person(id=6,name='Marcus Lee',role='Full-Stack Engineer',team='Enterprise Experience',location='New York, NY',skills=['React','TypeScript','Python','WebSocket'],capabilities=[Capability(name='Interactive UI',category='Experience',maturity=4),Capability(name='Real-Time Updates',category='Experience',maturity=3),Capability(name='API Integration',category='Platform',maturity=4)],summary='Builds full-stack internal applications with real-time data updates.')]
@app.middleware('http')
async def context(request:Request,call_next):
    rid=request.headers.get('x-request-id',str(uuid.uuid4()));t=time.perf_counter();resp=await call_next(request);resp.headers['x-request-id']=rid;log.info('request_id=%s method=%s path=%s status=%s duration_ms=%.2f',rid,request.method,request.url.path,resp.status_code,(time.perf_counter()-t)*1000);return resp
@app.get('/health')
def health():return {'status':'ok'}
@app.get('/api/people',response_model=list[Person])
def people(q:str=Query('',max_length=100),team:str=Query('',max_length=100),role:str=Query('',max_length=100),skill:str=Query('',max_length=100)):
    q=q.strip().lower()
    def ok(p):
        s=' '.join([p.name,p.role,p.team,p.location,*p.skills,*[c.name for c in p.capabilities]]).lower()
        return (not q or q in s) and (not team or p.team==team) and (not role or p.role==role) and (not skill or skill in p.skills)
    return [p for p in PEOPLE if ok(p)]
@app.get('/api/metadata',response_model=Metadata)
def metadata():return Metadata(teams=sorted({p.team for p in PEOPLE}),roles=sorted({p.role for p in PEOPLE}),skills=sorted({s for p in PEOPLE for s in p.skills}))
