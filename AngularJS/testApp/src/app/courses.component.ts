//this component is used to display the courses

import { Component } from '@angular/core';
import { CoursesService } from './courses.service';

@Component({
  selector: 'courses',
  template: `
    <h2>{{'Title: '+getTitle()}}</h2>
        <ul>
            <li *ngFor="let course of courses">
                {{course}}
            </li>
        </ul>
  `,
})

export class CoursesComponent {
    title = 'List of courses';
    courses;

    constructor(service: CoursesService) { //injecting the service
        //let service = new CoursesService();//buggy implementation
        this.courses = service.getCourses();
    }
    getTitle() {
        return this.title;
    }
}