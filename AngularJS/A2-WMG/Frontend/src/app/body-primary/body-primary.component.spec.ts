import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BodyPrimaryComponent } from './body-primary.component';

describe('BodyPrimaryComponent', () => {
  let component: BodyPrimaryComponent;
  let fixture: ComponentFixture<BodyPrimaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BodyPrimaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BodyPrimaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
