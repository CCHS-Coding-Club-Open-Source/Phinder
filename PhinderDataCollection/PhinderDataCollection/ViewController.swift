//
//  ViewController.swift
//  PhinderDataCollection
//
//  Created by Peter Maar on 11/4/17.
//  Copyright © 2017 alset333. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
//        let hoursFromGMT = Double(TimeZone.current.secondsFromGMT()) / 3600.0
        
        print("Timezone:", TimeZone.current.abbreviation()!)
        
        let date = Date()
        let calendar = Calendar.current
        let hour = calendar.component(.hour, from: date)
        let minutes = calendar.component(.minute, from: date)
        
        
        print(date, "\n", calendar, "\n", hour, "\n", minutes)
        
        let prefLangCode = Locale.preferredLanguages
        print(prefLangCode)
        print(Locale.isoLanguageCodes)
        
        
        
        let identifiers : NSArray = NSLocale.availableLocaleIdentifiers as NSArray
        let locale = NSLocale(localeIdentifier: "en_US")
        let list = NSMutableString()
        for identifier in identifiers {
            let name = locale.displayName(forKey: NSLocale.Key.identifier, value: identifier)!
            list.append("\(identifier)\t\(name)\n")
        }
        
        print(list)
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

