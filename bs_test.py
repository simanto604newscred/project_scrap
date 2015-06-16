from lxml import etree

def main():

    table = etree.XML ("""
<table id="results-table" class="table table-bordered table-striped table-hover tablesorter">
          <thead class="table-header">
            <tr>
              <th id="th-hash" class="span1">#</th>
              <th class="name-col span2">Name</th>
              <th class="span1">Age</th>
              <th id="th-cities" class="span2">Cities</th>
              <th id="th-relatives" class="span2">Relatives</th>
              <!-- <th id="th-phone" class="th-center span1">Phone</th>
              <th id="th-address" class="th-center span1">Address</th> -->
              <th id="th-view-btn" class="th-center span2">Report</th>
            </tr>
          </thead>
          <tbody data-fr-iterated="teasers" data-fr-bound="searchData teaserData" data-fr-template="6" data-fr-sorted="teaserSorter" data-fr-mapped="TeaserRecord" id="results"><tr data-fr-bound2="searchData teaserData.teasers[1]" data-fr-map="TeaserRecord" data-fr-sort="teaserSorter" data-fr-click="store currentRecord" class="results-row">
              <td class="td-hash">
                <span class="index-col">1</span>
              </td>
              <td class="name-col">
                <a href="#" class="name-found">David R Balogh</a>
                <div class="place-single">
                  Miami, FL
                </div>
                <div class="hidden-phone">
                  <ul class="aka-list">

                    <li class="aka-list-heading">Also Seen As</li>


                    <li>- David Balough</li>

                  </ul>
                </div>
              </td>
              <td class="age-col">
                94
              </td>
              <td>
                <ul>

                  <li>Miami, FL</li>

                  <li>Carlsbad, CA</li>

                  <li>Miami Beach, FL</li>

                  <li>Bal Harbour Village, FL</li>

                  <li>Bal Harbour, FL</li>

                </ul>
              </td>
              <td>
                <ul>

                  <li>Andrew Balogh</li>

                  <li>Cara Hope Balogh</li>

                  <li>David R Balogh</li>

                  <li>Sallie R Balogh</li>

                  <li>Robert B Balough</li>

                </ul>
              </td>
             <!-- <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td>
              <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td> -->
               <td class="report-col align-center">
                <a href="#" class="btn-block aux-btn generate_report_from_teaser text-center">THAT'S THE ONE</a>
              </td>
            </tr><tr data-fr-bound2="searchData teaserData.teasers[6]" data-fr-map="TeaserRecord" data-fr-sort="teaserSorter" data-fr-click="store currentRecord" class="results-row">
              <td class="td-hash">
                <span class="index-col">2</span>
              </td>
              <td class="name-col">
                <a href="#" class="name-found">David R Balogh</a>
                <div class="place-single">
                  Carlsbad, CA
                </div>
                <div class="hidden-phone">
                  <ul class="aka-list">


                  </ul>
                </div>
              </td>
              <td class="age-col">

              </td>
              <td>
                <ul>

                  <li>Carlsbad, CA</li>

                  <li>Miami Beach, FL</li>

                  <li>Bal Harbour Village, FL</li>

                  <li>Bal Harbour, FL</li>

                </ul>
              </td>
              <td>
                <ul>

                  <li>David R Balogh</li>

                  <li>Sallie R Balogh</li>

                </ul>
              </td>
             <!-- <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td>
              <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td> -->
               <td class="report-col align-center">
                <a href="#" class="btn-block aux-btn generate_report_from_teaser text-center">THAT'S THE ONE</a>
              </td>
            </tr><tr data-fr-bound2="searchData teaserData.teasers[2]" data-fr-map="TeaserRecord" data-fr-sort="teaserSorter" data-fr-click="store currentRecord" class="results-row">
              <td class="td-hash">
                <span class="index-col">3</span>
              </td>
              <td class="name-col">
                <a href="#" class="name-found">David R Balogh</a>
                <div class="place-single">
                  Miami, FL
                </div>
                <div class="hidden-phone">
                  <ul class="aka-list">

                    <li class="aka-list-heading">Also Seen As</li>


                    <li>- Balogh Robbins</li>

                  </ul>
                </div>
              </td>
              <td class="age-col">

              </td>
              <td>
                <ul>

                  <li>Miami, FL</li>

                  <li>Miami Beach, FL</li>

                </ul>
              </td>
              <td>
                <ul>

                </ul>
              </td>
             <!-- <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td>
              <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td> -->
               <td class="report-col align-center">
                <a href="#" class="btn-block aux-btn generate_report_from_teaser text-center">THAT'S THE ONE</a>
              </td>
            </tr><tr data-fr-bound2="searchData teaserData.teasers[0]" data-fr-map="TeaserRecord" data-fr-sort="teaserSorter" data-fr-click="store currentRecord" class="results-row">
              <td class="td-hash">
                <span class="index-col">4</span>
              </td>
              <td class="name-col">
                <a href="#" class="name-found">David Sally Balogh</a>
                <div class="place-single">
                  Miami, FL
                </div>
                <div class="hidden-phone">
                  <ul class="aka-list">


                  </ul>
                </div>
              </td>
              <td class="age-col">

              </td>
              <td>
                <ul>

                  <li>Miami, FL</li>

                </ul>
              </td>
              <td>
                <ul>

                </ul>
              </td>
             <!-- <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td>
              <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td> -->
               <td class="report-col align-center">
                <a href="#" class="btn-block aux-btn generate_report_from_teaser text-center">THAT'S THE ONE</a>
              </td>
            </tr><tr data-fr-bound2="searchData teaserData.teasers[3]" data-fr-map="TeaserRecord" data-fr-sort="teaserSorter" data-fr-click="store currentRecord" class="results-row">
              <td class="td-hash">
                <span class="index-col">5</span>
              </td>
              <td class="name-col">
                <a href="#" class="name-found">David R Balogh</a>
                <div class="place-single">
                  Miami Beach, FL
                </div>
                <div class="hidden-phone">
                  <ul class="aka-list">


                  </ul>
                </div>
              </td>
              <td class="age-col">

              </td>
              <td>
                <ul>

                  <li>Miami Beach, FL</li>

                </ul>
              </td>
              <td>
                <ul>

                </ul>
              </td>
             <!-- <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td>
              <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td> -->
               <td class="report-col align-center">
                <a href="#" class="btn-block aux-btn generate_report_from_teaser text-center">THAT'S THE ONE</a>
              </td>
            </tr><tr data-fr-bound2="searchData teaserData.teasers[4]" data-fr-map="TeaserRecord" data-fr-sort="teaserSorter" data-fr-click="store currentRecord" class="results-row">
              <td class="td-hash">
                <span class="index-col">6</span>
              </td>
              <td class="name-col">
                <a href="#" class="name-found">David Ballah</a>
                <div class="place-single">
                  Miami, FL
                </div>
                <div class="hidden-phone">
                  <ul class="aka-list">


                  </ul>
                </div>
              </td>
              <td class="age-col">

              </td>
              <td>
                <ul>

                  <li>Miami, FL</li>

                </ul>
              </td>
              <td>
                <ul>

                </ul>
              </td>
             <!-- <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td>
              <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td> -->
               <td class="report-col align-center">
                <a href="#" class="btn-block aux-btn generate_report_from_teaser text-center">THAT'S THE ONE</a>
              </td>
            </tr><tr data-fr-bound2="searchData teaserData.teasers[5]" data-fr-map="TeaserRecord" data-fr-sort="teaserSorter" data-fr-click="store currentRecord" class="results-row">
              <td class="td-hash">
                <span class="index-col">7</span>
              </td>
              <td class="name-col">
                <a href="#" class="name-found">David R Balogh</a>
                <div class="place-single">
                  Miami, FL
                </div>
                <div class="hidden-phone">
                  <ul class="aka-list">


                  </ul>
                </div>
              </td>
              <td class="age-col">

              </td>
              <td>
                <ul>

                  <li>Miami, FL</li>

                </ul>
              </td>
              <td>
                <ul>

                </ul>
              </td>
             <!-- <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td>
              <td>

                <div class="wrap-icon">
                  <i class="icon-yes-check"> </i>
                </div>

              </td> -->
               <td class="report-col align-center">
                <a href="#" class="btn-block aux-btn generate_report_from_teaser text-center">THAT'S THE ONE</a>
              </td>
            </tr></tbody>
        </table>""")

    import ipdb;ipdb.set_trace()
    # table = ET.XML(s)
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    for row in rows:
        values = [col.text for col in row]
        print dict(zip(headers, values))

if __name__ == '__main__':
    main()